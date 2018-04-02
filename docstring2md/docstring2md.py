#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# docstring2md
## Description:

This package Export Google DocString to Markdown from Python module.

The following files comprise the `docstring2md` package:
* `LICENSE`: The license file. `docstring2md` is released under the terms of
the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.

The package contents itself are in the config_from_json directory:
* `__ init __.py` Initialization file for the Python package.
* `docstring2md/docstring2md.py`: The code of interest.

## Setup:

    git clone https://github.com/francois-le-ko4la/docstring2md.git
    cd config-from-json
    sudo make install

## Test:

This module has been tested and validated on Ubuntu.

    sudo make test

## How to use this Class:

To be continued...

## Todo:

- [X] Create the project
- [X] Write code and tests
- [ ] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [ ] Validate features
- [ ] Write Doc/stringdoc
- [ ] Run PEP8 validation
- [ ] Clean & last check
- [ ] Release

## Note:
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import os
import sys
import string
import inspect
import importlib.util
import getopt

class DocString2MD(object):

    """
    Class documentation
    """

    def __init__(self, module_name):
        """
        """
        sys.path.append(os.getcwd())
        #print(os.getcwd())
        self.__module_name = module_name
        self.__module = None
        self.__module_spec = None
        self.__output = ""
        self.__firstItem = True

    def check_module(self):
        """
        Checks if module can be imported without actually
        importing it
        """
        self.__module_spec = importlib.util.find_spec(self.__module_name)
        if self.__module_spec is None:
            print('Module: {} not found'.format(self.__module_name))
            return False
        else:
            # print('Module: {} can be imported!'.format(self.__module_name))
            return True

    def import_module_from_spec(self):
        """
        Import the module via the passed in module specification
        Returns the newly imported module
        """
        self.__module = importlib.util.module_from_spec(self.__module_spec)
        self.__module_spec.loader.exec_module(self.__module)

    def getdoc(self, obj):
        doc = inspect.getdoc(obj)
        if doc is None:
            return ""
        return doc

    def extract_docstring(self):
        """
        extract all
        """
        self.__output += self.getdoc(self.__module)
        self.__output += "\n\n## Dev docstring\n"
        self.__extract_class_docstring(self.__module)
        self.__extract_function_docstring(self.__module)
        # print(self.__output)

    def __generate_func_doc(self, func, class_member=False):

        func_name = ""
        if class_member:
            func_name = "#"

        func_name += "### Function {0}{1}:".format(
            (str(func['full_name']).split(" "))[1], func['args'])

        return "{0}\n\n```\n{1}\n```\n\n".format(func_name, func['doc'])

    def __generate_class_doc(self, clas):
        self.__output += "### Class {0}:\n{1}\n\n".format(clas[0],
                                                          self.getdoc(clas[1]))

    def __extract_function_docstring(self, item, class_member=False):
        """
        zjedaé azjd ajkzd
        """
        for func in inspect.getmembers(item, inspect.isfunction):
            self.__output += self.__generate_func_doc(
                {'name': func[0],
                 'args': str(inspect.signature(func[1])),
                 'full_name': func[1],
                 'doc': self.getdoc(func[1])
                 },
                class_member)

    def __extract_class_docstring(self, item):
        for cl in inspect.getmembers(item, inspect.isclass):
            if cl[0] != "__class__":
                # self.__output += "\n\n**** class_header"
                # self.__output += cl[0]
                # self.__output += inspect.getdoc(cl[1])
                self.__generate_class_doc(cl)
                self.__extract_function_docstring(cl[1], class_member=True)
                # self.__extract_class_docstring(cl[1])

    def get(self):
        return self.__output
