#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A setuptools based setup module.

Example:
    ./python test
    ./python install

Test:
    This script has been tested and validated on Ubuntu.

"""
from setuptools import setup, find_packages
from setuptools.config import read_configuration
import warnings


warnings.filterwarnings("ignore")
CFG = read_configuration('./setup.cfg')
CFG["options"].update(CFG["metadata"])
CFG = CFG["options"]
setup(use_scm_version=False, **CFG)
