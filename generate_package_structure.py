"""
Using a model package and the name of your future package, will create a minimal package structure to be used

This model contain a gitlab-ci configuration, a gitignore, a setup.py, some utils functions not available by default, etc...
"""

import argparse
import shutil
import os

reference_folder = "model_package"

package_tag = "<my_mackage>"  # String to be searched and replace by the future package name



def copy_directory(ref_folder, dest_folder):
    """
    Copy directory recursively to create a new package from the model package

    :param str ref_folder: Name of the reference folder to copy data from
    :param str dest_folder: Name of destination folder
    :return:
    """

    # remove destination folder if exists
    if os.path.isdir(dest_folder):
        shutil.rmtree(dest_folder)

    shutil.copytree(ref_folder, dest_folder)
