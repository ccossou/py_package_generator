import pkg_resources
import configobj
import validate
import sys
import os
import logging

LOG = logging.getLogger(__name__)


def get_nested(data, args):
    """
    Allow to get value in dictionnary tree

    Used in ConfigObj validator

    If ones want to get toto["section1"]["s2]["key"]
    call:
    value = get_nested(toto, ["section1", "s2", "key"])

    Parameter:
    :param dict data: input dict to get data on
    :param list(str) args: list of keys to use recursively

    :return: value corresponding to the list of keys
    """
    value = data.copy()
    for key in args:
        value = value.get(key)

    return value


def get_config(filename):
    """
    Read then validate and convert the input file

    :param str filename: .ini filename

    :return ConfigObj:  config file
    """

    if not os.path.isfile(filename):
        LOG.error("The file '{}' can't be found".format(filename))
        sys.exit()

    # Prepare to convert values in the config file
    val = validate.Validator()
    specfile = pkg_resources.resource_filename('<my_package>', 'configspec.ini')
    configspec = configobj.ConfigObj(specfile, list_values=False)

    config = configobj.ConfigObj(filename, configspec=configspec, raise_errors=True)

    # Check and convert values in config.ini (i.e str to float or integer/bool)
    results = config.validate(val, preserve_errors=True)

    for entry in configobj.flatten_errors(config, results):

        [section_list, key, error] = entry
        section_list.append(key)

        if not error:
            msg = "The parameter %s was not in the config file\n" % key
            msg += "Please check to make sure this parameter is present and there are no mis-spellings."
            raise ValueError(msg)

        if key is not None and isinstance(error, validate.VdtValueError):
            option_string = get_nested(configspec, section_list)
            msg = "The parameter {} was set to {} which is not one of the allowed values\n".format(
                key, get_nested(config, section_list))
            msg += "Please set the value to be in {}".format(option_string)
            raise ValueError(msg)

    return config
