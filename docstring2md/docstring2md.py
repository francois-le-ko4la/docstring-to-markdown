#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

____                 _        _             ____  __  __ ____
|  _ \  ___   ___ ___| |_ _ __(_)_ __   __ _|___ \|  \/  |  _ \
| | | |/ _ \ / __/ __| __| '__| | '_ \ / _` | __) | |\/| | | | |
| |_| | (_) | (__\__ \ |_| |  | | | | | (_| |/ __/| |  | | |_| |
|____/ \___/ \___|___/\__|_|  |_|_| |_|\__, |_____|_|  |_|____/
                                       |___/

"""
import os
import sys
import inspect
import importlib.util
from functools import wraps
import re


class DocString2MD(object):

    """
    Class DocString2MD : export Google docstring to MD File.
    """

    def __init__(self, module_name, export_file=None):
        """Init the class
        This function define default attributs.

        Args:
            module_name (str): /path/to/the/module/
            export_file (str): /path/to/the/doc/file - None by default

        Attributes:
            self.__module_name
            self.__module
            self.__module_spec
            self.__output
            self.__first_member

        Returns:
            obj

        """
        sys.path.append(os.getcwd())
        self.__module_name = module_name
        self.__module = None
        self.__module_spec = None
        self.__output = ""
        self.__first_member = True
        self.__exportfile = export_file

    def __check_module(func):
        """
        Decorator - Checks if module can be imported.
        Updates self.__module_spec in order to import the module.

        Args:
            None

        Retuns:
            bool: The return value. True for success, False otherwise.

        """

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """ wrapper """
            try:
                self.__module_spec = importlib.util.find_spec(
                    self.__module_name)
                if self.__module_spec is None:
                    return False
            except Exception as e:
                print("This file is not a module.")
                return False
            return func(self, *args, **kwargs)
        return wrapper

    @__check_module
    def import_module(self):
        """
        Check module
        Import the module via the passed in module specification
        Returns the newly imported module and updates attributes self.__module

        Args:
            None

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        try:
            self.__module = importlib.util.module_from_spec(self.__module_spec)
            self.__module_spec.loader.exec_module(self.__module)
        except Exception as e:
            print("Import error")
            return False
        return True

    def get_doc(self):
        """

        Extract the doc
        Returns self.__output or self.__writedoc

        Args:
            None

        Returns:
            str: self.__output
        """

        self.__extract(self.__module)

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

    def __replace_string(old_string, new_string):
        """
        Decorator - search & replace a string by another string
        Example : replace space by a HTML tag.

        Args:
            old_string (str): string to search
            new_string (str): new string

        Returns:
            decorated function

        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                """ wrapper """
                return (func(*args, **kwargs)).replace(old_string, new_string)
            return func_wrapper
        return tags_decorator

    def __replace_beginning_and_end(begin_regexp, end_regexp,
                                    begin_tag, end_tag):
        """
        Decorator - replace the beggining and the end

        Example:
            All new lines must be provided with a specific tag
            > 'Line' <br />

        Args:
            begin_regexp (str)
            end_regexp (str)
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function
        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                """ wrapper """
                return re.sub(
                    begin_regexp+'(.*)'+end_regexp,
                    begin_tag + r'\1' + end_tag,
                    func(*args, **kwargs),
                    flags=re.MULTILINE
                    )
            return func_wrapper
        return tags_decorator

    def __md_tag(begin_tag, end_tag):
        """
        Decorator - add a tag

        Example:
            ('__', '__') => __ TXT __

        Args:
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function
        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                """ wrapper """
                return "{0}{1}{2}".format(
                    begin_tag, func(*args, **kwargs), end_tag)
            return func_wrapper
        return tags_decorator

    @__replace_beginning_and_end('^', '$', '> ', '<br />')
    @__replace_beginning_and_end('^', ':$', '<b>', ':</b>')
    @__replace_string('    ', '&nbsp;' * 15 + '  ')
    @__md_tag("\n", "\n")
    def __getdoc(self, member):
        """
        Use inspect.getdoc
        If docstring is not usable returns an empty string.
        This function is decorated to provide MD tags.

        Args:
            member: inspect object

        Returns:
            str: docstring

        """
        doc = inspect.getdoc(member[1])
        if doc is None:
            return ""
        return doc

    def __get_member_name(self, member):
        """
        Provide the member name

        Example:
            function -> name(args)
            classe -> name()

        Args:
            member: inspect object

        Returns:
            str
        """
        if inspect.isclass(member[1]):
            return "{0}()".format(str(member[0]))
        else:
            return "{0}{1}".format((str(member[1]).split(" "))[1],
                                   str(inspect.signature(member[1])))

    @__md_tag("\n\n", "\n")
    def __get_member_title(self, member, level):
        """
        Provide the member title with MD TAG
        """
        return "#"*(level+2) + " " + self.__get_member_name(member)

    @__md_tag("def ", ":")
    def __get_function_def(self, member):
        """
        Provide the full function def.
        Example:
            'def name(args):'
        """
        return self.__get_member_name(member)

    @__md_tag("class ", ":")
    def __get_class_def(self, member):
        """
        Provide the full class def.
        Example:
            'class name():'
        """
        return self.__get_member_name(member)

    @__md_tag("\n````python\n", "\n````\n\n")
    def __get_member_def(self, member):
        """
        Provide the member def and add MD tag.
        """
        if inspect.isclass(member[1]):
            return self.__get_class_def(member)
        else:
            return self.__get_function_def(member)

    def __create_doc(self, member, level):
        """
        Updates self.__output according to args provided.

        Args:
            member (obj): inspect object
            member_isclass (bool): False by default / if class -> True
            class_member (bool): False by default / if def in class -> True

        Returns:
            None

        """
        if self.__first_member:
            self.__first_member = False
            self.__output += inspect.getdoc(self.__module)
            self.__output += "\n\n## Dev docstring\n"

        self.__output += self.__get_member_title(member, level)
        self.__output += self.__get_member_def(member)
        self.__output += self.__getdoc(member)

    def __extract(self, item, level=0):
        """
        Inspects functions in a moddule.
        Call self.__create_doc()

        Args:
            item (obj): inspect obect
            class_member (bool): False by default / if def in class -> True

        Returns:
            None
        """
        if level >= 2:
            return

        level += 1
        for member in inspect.getmembers(item):
            if inspect.isclass(member[1]) and member[0] != "__class__":
                self.__create_doc(member, level)
                self.__extract(member[1], level)
            if inspect.isfunction(member[1]):
                self.__create_doc(member, level)
