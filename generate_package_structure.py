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


def create_new_package(ref_folder, package_name, package_tag):
    """
    Copy directory recursively to create a new package from the model package

    :param str ref_folder: Name of the reference folder to copy data from
    :param str dest_folder: Name of destination folder
    :return:
    """

    dest_folder = os.path.join("generated", package_name)

    # remove destination folder if exists
    if os.path.isdir(dest_folder):
        shutil.rmtree(dest_folder)

    # Create partial function that only take src and dst for arguments
    custom_copy = functools.partial(copy_with_replace, str1=package_tag, str2=package_name)

    shutil.copytree(ref_folder, dest_folder, copy_function=custom_copy)


def copy_with_replace(src, dst, str1, str2):
    """
    Copy file but replace str1 by str2 every time it's found.

    This function is designed to be used on shutil.copytree in place of the default copy function

    :param src: Source file
    :param dst: destination file
    :param str1: string to be searched for
    :param str2: replacement string
    :return:
    """

    with open(src, 'r') as obj:
        s = obj.read()

    s = s.replace(str1, str2)

    with open(dst, 'w') as obj:
        obj.write(s)


reference_folder = "model_package"
package_tag = "<my_package>"  # String to be searched and replace by the future package name

create_new_package(ref_folder=reference_folder, package_name="toto", package_tag=package_tag)
