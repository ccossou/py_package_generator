#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Using a model package and the name of your future package, will create a minimal package structure to be used

This model contain a gitlab-ci configuration, a gitignore, a setup.py, some utils functions not available by default, etc...
"""

import argparse
import shutil
import os
import functools
import sys

#minimum_version = (3, 2)
#assert sys.version_info >= minimum_version, "You must use Python >= {}.{}".format(*minimum_version)

def create_new_package(ref_folder, package_name, package_tag, overwrite=True):
    """
    Copy directory recursively to create a new package from the model package

    :param str ref_folder: Name of the reference folder to copy data from
    :param str dest_folder: Name of destination folder
    :return:
    """

    dest_folder = "generated"

    # remove destination folder if exists.
    # If not, will add info to the existing directory
    if overwrite and os.path.isdir(dest_folder):
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

    #shutil.copytree(ref_folder, dest_folder, copy_function=custom_copy, ignore=shutil.ignore_patterns())


def copy_with_replace(src, dst, str1, str2, merge=False):
    """
    Copy file but replace str1 by str2 every time it's found.

    This function is designed to be used on shutil.copytree in place of the default copy function

    :param src: Source file
    :param dst: destination file
    :param str1: string to be searched for
    :param str2: replacement string
    :param bool merge: If True, will append first file to
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



def combine_files(original_file, add_on_file):
    """
    When adding a plugin, if a file already exist, will merge both codes (plugin one added at the end of the original)

    :param str original_file:
    :param str add_on_file:
    :return:
    """

def add_plugin(plugin_folder, package_name):
    """
    Add necessary files to add an .ini file reader into the future package

    A plugin folder must have the same structure as the original package

    :param str ref_folder:
    :param str package_name:
    :return:
    """

    dest_folder = "generated"

    # Create partial function that only take src and dst for arguments
    custom_copy = functools.partial(copy_with_replace, str1=package_tag, str2=package_name)

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



reference_folder = "model_package"
package_tag = "<my_package>"  # String to be searched and replace by the future package name

create_new_package(ref_folder=reference_folder, package_name="toto", package_tag=package_tag)

