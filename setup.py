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
import os
from setuptools import setup
from setuptools.config import read_configuration
import warnings


warnings.filterwarnings("ignore")

cfg = read_configuration('./setup.cfg')
# print(cfg)
cfg["options"].update(cfg["metadata"])
cfg = cfg["options"]
setup(use_scm_version=False, **cfg)
