# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import wed
version = wed.__version__

setup(
    name='wed',
    version=version,
    author='',
    author_email='a@g.v',
    packages=[
        'wed',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['wed/manage.py'],
)