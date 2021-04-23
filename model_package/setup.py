#!/usr/bin/env python

"""
Setup file
"""

from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    package_data={},
    scripts=[],
    data_files=[('', ['README.adoc'])]
)
