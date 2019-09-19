#!/usr/bin/env python

"""
Setup file for installing parallel pipeline
"""

import io
import os
import re

from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="<my_package>",
    version=find_version("<my_package>", "version.py"),
    description="",
    url="",
    author="",
    author_email="",
    packages=find_packages(),
    package_data={},
    scripts=[],
    data_files=[('', ['README.adoc'])]
)
