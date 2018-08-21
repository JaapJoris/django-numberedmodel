#!/usr/bin/env python
import os, sys
from setuptools import setup, find_packages

setup(
    name = 'django-numberedmodel',
    version = '0.1.4',
    url = 'https://github.com/JaapJoris/django-numberedmodel',
    author = 'Jaap Joris Vens',
    author_email = 'jj@rtts.eu',
    license = 'GPL3',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'django >= 1.7.7',
    ],
)
