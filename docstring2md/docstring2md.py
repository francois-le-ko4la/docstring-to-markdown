#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import string
import inspect
import importlib.util
import getopt


class DocString2MD(object):

    """
    Class DocString2MD : export Google docstring to MD File.
    """

    def __init__(self, module_name, export_file=None):
        """Init the ConfigFromJson Class
        This function define default attributs.

        Args:
            module_name (str): /path/to/the/module/

        Attributes:
            self.__module_name
            self.__module
            self.__module_spec
            self.__output
            self.__firstItem

        Returns:
            obj

        """
        sys.path.append(os.getcwd())
        self.__module_name = module_name
        self.__module = None
        self.__module_spec = None
        self.__output = ""
        self.__firstItem = True
        self.__exportfile = export_file

    def check_module(self):
        """
        Checks if module can be imported without actually importing it.
        Updates self.__module_spec in order to import the module.

        Args:
            None

        Retuns:
            bool: The return value. True for success, False otherwise.

        """
        self.__module_spec = importlib.util.find_spec(self.__module_name)
        if self.__module_spec is None:
            print('Module: {} not found'.format(self.__module_name))
            return False
        else:
            return True

    def import_module(self):
        """
        Import the module via the passed in module specification
        Returns the newly imported module and updates attributes self.__module

        Args:
            None

        Returns:
            None

        """
        self.__module = importlib.util.module_from_spec(self.__module_spec)
        self.__module_spec.loader.exec_module(self.__module)

    def extract_doc(self):
        """
        Extract docstring inside the module and updates self.__output:
        - Header
        - Class
        - Functions

        Args:
            None

        Returns:
            None
        """
        self.__output += self.__getdoc(self.__module)
        self.__extract_class(self.__module)
        self.__extract_function(self.__module)

    def get_doc(self):
        """
        Returns self.__output

        Args:
            None

        Returns:
            str: self.__output
        """
        if self.__exportfile is None:
            return self.__output
        else:
            return self.__writedoc()

    def __writedoc(self):
        """
        Writes the content in the file

        args:
            None

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        try:
            exportfile = open(self.__exportfile, "w")
            try:
                exportfile.write(self.__output)
            finally:
                exportfile.close()
        except IOError:
            print("Unable to create {0} on disk.".format(self.__exportfile))
            return False

        return True

    def __getdoc(self, obj):
        """
        Call inspect.getdoc with obj parameter.
        If docstring is not usable returns an empty string.

        Args:
            None

        Returns:
            str: docstring

        """
        doc = inspect.getdoc(obj)
        if doc is None:
            return ""
        return doc

    def __create_doc(self, member, member_isclass=False, class_member=False):
        """
        Updates self.__output according to args provided.

        Args:
            member (obj): inspect object
            member_isclass (bool): False by default / if class -> True
            class_member (bool): False by default / if def in class -> True

        Returns:
            None

        """
        if self.__firstItem:
            self.__firstItem = False
            self.__output += "\n\n## Dev docstring\n"

        if member_isclass:
            self.__output += "### Class {0}:\n{1}\n\n".format(member[0],
                    self.__getdoc(member[1]))
        else:
            func_name = ""
            if class_member:
                func_name = "#"

            func_name += "### Function {0}{1}:".format(
                                            (str(member[1]).split(" "))[1],
                                            str(inspect.signature(member[1]))
                                            )
            func_doc = self.__getdoc(member[1])

            self.__output += "{0}\n\n```\n{1}\n```\n\n".format(func_name,
                                                               func_doc
                                                               )

    def __extract_function(self, item, class_member=False):
        """
        Inspects functions in a moddule.
        Call self.__create_doc()

        Args:
            itms (obj): inspect obect
            class_member (bool): False by default / if def in class -> True

        Returns:
            None
        """
        for member in inspect.getmembers(item, inspect.isfunction):
            self.__create_doc(member, False, class_member)

    def __extract_class(self, module):
        """
        Inspects classes in a module
        Call self.__create_doc() & self.__extract_function()

        Args:
            module (obj): instpect object

        Returns:
            None

        """
        for member in inspect.getmembers(module, inspect.isclass):
            if member[0] != "__class__":
                self.__create_doc(member, member_isclass=True)
                self.__extract_function(member[1], class_member=True)
