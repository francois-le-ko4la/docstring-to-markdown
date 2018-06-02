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
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call
import sys


if not sys.version_info[0] == 3:
            sys.exit("Sorry, your Python is not supported (yet)")


def apt_get_install():
    check_call("sudo apt install -y graphviz".split())


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        apt_get_install()
        develop.run(self)


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        apt_get_install()
        install.run(self)


CFG = read_configuration('./setup.cfg')
CFG["options"].update(CFG["metadata"])
CFG = CFG["options"]
CFG["cmdclass"] = {
    'develop': PostDevelopCommand,
    'install': PostInstallCommand,
}
setup(**CFG)
