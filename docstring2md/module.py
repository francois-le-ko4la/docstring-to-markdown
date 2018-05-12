#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import inspect
import importlib.util
import pathlib
from functools import wraps
import sys
from docstring2md.objdef import PythonObj, ModuleObj
from docstring2md.__config__ import MyConst, LineType, PythonObjType


class ExtractPythonModule(object):

    """
    Object in order to extract Python functions, classes....

    Use:
        >>> mod = ExtractPythonModule("oups...")
        >>> mod.import_module()
        Traceback (most recent call last):
        ...
        ModuleNotFoundError: No module named 'oups'
        >>> mod = ExtractPythonModule("json")
        >>> mod.import_module()
        True
        >>> mod.extract()

    """

    def __init__(self, module_name, priv=False):
        """
        Init
        """
        self.__module_name = module_name
        self.__module = None
        self.__module_spec = None
        self.module = None
        self.__priv = priv

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
            self.__module_spec = importlib.util.find_spec(
                self.__module_name)
            if self.__module_spec is None:
                raise Exception("This file is not a module: {}".format(
                    self.__module_name))
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
            if self.__module_name in sys.modules:
                return True
            """ add module in sys.modules """
            importlib.import_module(self.__module_name)
        except Exception as e:
            raise Exception("Import error")
        return True

    def extract(self):
        """
        Defines module object and extracts all members.

        Args:
            None

        Returns:
            None
        """

        self.module = ModuleObj(
                self.__module_name,
                self.__module_name,
                inspect.getdoc(self.__module)
            )
        self.__extract(self.module, self.__module)

    def __findinline(self, line, search_item):
        if line.find(search_item) is 0:
            return True
        return False

    def __linetype(self, line):
        if self.__findinline(line, MyConst.decorator_tag):
            return LineType.decorator
        if self.__findinline(line, MyConst.function_tag):
            return LineType.function
        return LineType.other

    def __extractdecorator(self, member):
        sourcelines = inspect.getsourcelines(member[1])[0]
        decorator = ""
        result = dict()
        add_decorator = False
        for i, line in enumerate(sourcelines):
            line = line.strip()
            line_type = self.__linetype(line)

            if line_type is LineType.other:
                decorator = ""
                add_decorator = False
            if line_type is LineType.decorator:
                decorator += "{}\n".format(line)
                add_decorator = True
            if line_type is LineType.function:
                if add_decorator:
                    line = line.replace(
                            MyConst.function_tag,
                            "{}{}.".format(MyConst.function_tag, member[0])
                        )
                    result[line] = decorator
        return result

    def __extractproperties(self, my_pythonobj, inspectmembers,
                            level, decorator, cls_name):
        if level >= 2 or len(inspectmembers) is 0:
            return

        level += 1

        for current_property, inspect_obj in inspectmembers:
            full_name = ""
            name = ""
            docstring = None
            for current_func in decorator.keys():
                if "{}{}.{}(".format(MyConst.function_tag,
                                     cls_name,
                                     current_property) in current_func:
                    full_name += "{}{}\n".format(decorator[current_func],
                                                 current_func
                                                 )
                    if docstring is None:
                        docstring = inspect.getdoc(inspect_obj)
            name = "{}: {}.{}".format(
                MyConst.property_tag, cls_name, current_property)
            if full_name is not "":
                """
                not inheritance
                """
                new_pythonobj = PythonObj(
                        name,
                        full_name,
                        docstring or MyConst.property_tag,
                        level,
                        PythonObjType.fun
                    )
                my_pythonobj.members[name] = new_pythonobj

    def __extract(self, my_pythonobj, inspectmembers, level=0, decorator=None):
        """
        Inspects classes & functions in a moddule.
        Store information in a PythonObj object.

        Args:
            inspectmembers (obj): inspect obect
            my_pythonobj (PythonObj): object to define a Python member

        Returns:
            None
        """
        if level >= 2:
            return

        level += 1

        for member in inspect.getmembers(inspectmembers):
            if inspect.isclass(member[1]) and member[0] != "__class__":
                """ If external class -> stop """
                if self.__module_name not in str(member[1]):
                    return

                decorator = self.__extractdecorator(member)
                properties = inspect.getmembers(
                        member[1],
                        lambda o: isinstance(o, property)
                    )
                name = "{0}()".format(str(member[0]))
                full_name = inspect.getsourcelines(
                    member[1])[0][0].replace('\n', '')
                docstring = inspect.getdoc(member[1])
                new_pythonobj = PythonObj(name, full_name, docstring, level,
                                          PythonObjType.cla)
                my_pythonobj.members[name] = new_pythonobj

                self.__extractproperties(
                        new_pythonobj,
                        properties,
                        level,
                        decorator,
                        str(member[0])
                    )
                self.__extract(
                        new_pythonobj,
                        member[1],
                        level,
                        decorator
                    )
            if inspect.isfunction(member[1]):
                fun = (str(member[1]).split(" "))[1]
                funisprivate = "__" in fun
                if self.__priv is True or funisprivate is not True:
                    name = "{0}{1}".format((str(member[1]).split(" "))[1],
                                           str(inspect.signature(member[1])))

                    full_name = "{}{}:".format(MyConst.function_tag, name)
                    if decorator is not None and full_name in decorator:
                        full_name = "{}{}".format(
                                decorator[full_name],
                                full_name
                            )
                    docstring = inspect.getdoc(member[1])
                    new_pythonobj = PythonObj(
                            name,
                            full_name,
                            docstring,
                            level,
                            PythonObjType.fun
                        )
                    my_pythonobj.members[name] = new_pythonobj


if __name__ == "__main__":
    import doctest
    doctest.testmod()
