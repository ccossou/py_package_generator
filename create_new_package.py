#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Using a model package and the name of your future package, will create a minimal package structure to be used

This model contain a gitlab-ci configuration, a gitignore, a setup.py, some utils functions not available by default,
etc...
"""

import argparse
import shutil
import os
import functools
import sys

# The exist_ok option for os.makedirs appeared in Python 3.2
minimum_version = (3, 2)

reference_folder = "model_package"
package_tag = "{my_package}"  # String to be searched and replace by the future package name
valid_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def create_new_package(ref_folder, package_name, package_tag):
    """
    Copy directory recursively to create a new package from the model package

    :param str ref_folder: Name of the reference folder to copy data from
    :param str package_name: Name of the future package
    :param str package_tag: Generic and identifiable string to be search in the model directory/file.
    "{my_package}" is expected by default
    """

    # Directory were the generated package is stored
    dest_folder = "generated"

    # remove destination folder if exists.
    if os.path.isdir(dest_folder):
        shutil.rmtree(dest_folder)

    # Create partial function that only take src and dst for arguments
    custom_copy = functools.partial(copy_with_replace, str1=package_tag, str2=package_name)

    for root, dirs, files in os.walk(ref_folder):
        # Create empty dirs
        for d in dirs:
            dpath = os.path.join(root, d)
            dpath = dpath.replace(package_tag, package_name)
            dpath = dpath.replace(ref_folder, dest_folder)

            os.makedirs(dpath)

        # Copy files
        for f in files:
            fpath = os.path.join(root, f)

            dst_fpath = fpath.replace(ref_folder, dest_folder)
            dst_fpath = dst_fpath.replace(package_tag, package_name)

            custom_copy(fpath, dst_fpath)


def copy_with_replace(src, dst, str1, str2, merge=False):
    """
    Copy file but replace str1 by str2 every time it's found.

    This function is designed to be used on shutil.copytree in place of the default copy function

    :param src: Source file
    :param dst: destination file
    :param str1: string to be searched for
    :param str2: replacement string
    :param bool merge: If True, will append first file to the existing one
    :return:
    """

    write_mode = 'w'

    if merge:
        write_mode = 'a'

    with open(src, 'r') as obj:
        s = obj.read()

    s = s.replace(str1, str2)
    new_dst = dst.replace(str1, str2)

    with open(new_dst, write_mode) as obj:
        obj.write(s)


def add_plugin(plugin_folder, package_name):
    """
    Add necessary files to add an .ini file reader into the future package

    A plugin folder must have the same structure as the original package

    :param str plugin_folder: Name of the folder where the plugin files are in
    :param str package_name: Name of the generated package to modify
    :return:
    """

    dest_folder = "generated"

    # Create partial function that only take src and dst for arguments
    custom_copy = functools.partial(copy_with_replace, str1=package_tag, str2=package_name, merge=True)

    for root, dirs, files in os.walk(plugin_folder):
        # Create empty dirs
        for d in dirs:
            dpath = os.path.join(root, d)
            dpath = dpath.replace(package_tag, package_name)
            dpath = dpath.replace(plugin_folder, dest_folder)

            os.makedirs(dpath, exist_ok=True)

        # Copy files
        for f in files:
            fpath = os.path.join(root, f)

            dst_fpath = fpath.replace(plugin_folder, dest_folder)
            dst_fpath = dst_fpath.replace(package_tag, package_name)

            custom_copy(fpath, dst_fpath)


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Name of the future package (lowercase)", type=str, required=True)
parser.add_argument("-i", "--ini", help="Add the ini_file plugin for configuration file into the package",
                    action='store_true')
parser.add_argument("-g", "--gui", help="Add the GUI plugin into the package",
                    action='store_true')
args = parser.parse_args()

assert sys.version_info >= minimum_version, "You must use Python >= {}.{}".format(*minimum_version)

# Force lower case
package_name = args.name.lower()

# Check if all characters are valid
if not all(c in valid_characters for c in package_name):
    raise ValueError("Valid characters for package name are: {}".format("".join(valid_characters)))

# Check if first character is valid
if not package_name[0].isalpha():
    raise ValueError("First character of package name ('{}') needs to be a letter".format(package_name))

create_new_package(ref_folder=reference_folder, package_name=package_name, package_tag=package_tag)

if args.ini:
    add_plugin(plugin_folder="ini_file_plugin", package_name=package_name)

if args.gui:
    add_plugin(plugin_folder="gui_plugin", package_name=package_name)
