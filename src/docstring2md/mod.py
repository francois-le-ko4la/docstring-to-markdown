#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
from __future__ import annotations

import importlib
import pkgutil
from collections import deque
from typing import Union

from docstring2md.__config__ import LOGGING_MSG
from docstring2md.ast_engine import ObjVisitor, NodeListType
from docstring2md.file import MyFile
from docstring2md.log import logger


class PytMod:
    """
    Object in order to extract Python functions, class....

    Examples:
        >>> mod = PytMod("oups...")
        >>> mod.read()
        Traceback (most recent call last):
        ...
        ModuleNotFoundError: No module named 'oups'
        >>> mod = PytMod("json")
        >>> mod.read()
        >>> print(mod.node_lst[0].definition)
        def dump(obj, fp, **kw):
        >>> mod = PytMod(__file__)
        >>> mod.read()
        >>> print(mod.node_lst[0].docstring)
        This script is free software; you can redistribute it and/or
        modify it under the terms of the GNU Lesser General Public
        License as published by the Free Software Foundation; either
        ...
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
        >>> mod = PytMod('docstring2md')
        >>> mod.read()
        >>> print(mod.node_lst[0].definition)
        class Const(NamedTuple):

    """
    __path: Union[str, None]
    __module: str
    __private_def: bool

    def __init__(self, module_name: str, private_def: bool = False) -> None:
        self.__path = ""
        self.__module = module_name
        self.__private_def = private_def
        self.__node_lst: NodeListType = deque()
        logger.debug(LOGGING_MSG.pytmod.debug, module_name)

    @property
    def module(self) -> str:
        """
        module name (str):
            modulename
            /path/to/the/mod
            ./path/to/the/mod
        """
        return self.__module

    @property
    def node_lst(self) -> NodeListType:
        """
        returns all the docstrings.

        Returns:
                    str: Docstring

        """
        return self.__node_lst

    @property
    def pkg_main_docstring(self) -> NodeListType:
        """
        PKG only.

        Returns:
            str: Main docstring

        """
        if self.ismodule():
            logger.debug(LOGGING_MSG.pytmod_mod.info, self.module)
            return deque()
        logger.debug(LOGGING_MSG.pytmod_script.info, self.module)
        return self.__get_doc_from_module(
            f"{self.__path}/__init__.py", module_docstring=True)

    def ismodule(self) -> bool:
        """
        If module name is a module file => True
        Else if the module name is a package => False

        Returns:
            bool: It exits True on success, and False otherwise.

        """
        if self.module.endswith(".py"):
            return True
        return False

    def read(self) -> None:
        """
        Reads all files and store the result.

        Returns:
            None

        """
        logger.info(LOGGING_MSG.pytmod.info, self.module)
        if self.ismodule():
            logger.info(LOGGING_MSG.pytmod_mod.info, self.module)
            self.__node_lst += self.__get_doc_from_module(
                self.module, module_docstring=True)
        else:
            logger.info(LOGGING_MSG.pytmod_script.info, self.module)
            self.__node_lst += self.__get_doc_from_pkg(self.module)

    def __get_doc_from_module(
            self, module: str, module_docstring: bool = False) \
            -> NodeListType:
        # module name, for example json
        source = MyFile.set_path(module)
        # create an ObjVisitor to search in the module
        doc: ObjVisitor = ObjVisitor(
            module_docstring=module_docstring,
            private_def=self.__private_def
        )
        # Visit all module in the package
        doc.visit(doc.parse(source.read()))

        return doc.node_lst

    def __get_module_list(self, package: str) -> list[str]:
        module = []
        # Import the module
        imp_pkg = importlib.import_module(package)
        # keep the original path
        if self.__path == "":
            self.__path = imp_pkg.__path__[0]
        # Fix __init__ (walk_packages issue)
        init_file = MyFile.set_path(f"{imp_pkg.__path__[0]}/__init__.py")
        if init_file.exists:
            module = [str(init_file.path)]
        # use walk_packages to list all modules
        for _importer, modname, ispkg in pkgutil.walk_packages(
                imp_pkg.__path__):
            fullname = f"{package}.{modname}"
            if ispkg:
                logger.info(
                    LOGGING_MSG.new_module.info, fullname)
                module += self.__get_module_list(fullname)
            else:
                # if modname.startswith("__") is False:
                module.append(f"{imp_pkg.__path__[0]}/{modname}.py")
        return module

    def __get_doc_from_pkg(self, package: str) -> NodeListType:
        node_lst: NodeListType = deque()
        # get all modules
        modules = self.__get_module_list(package)
        logger.debug(LOGGING_MSG.pytmod_script.debug, str(modules))
        # read all modules and get all nodes
        for module in modules:
            logger.info(LOGGING_MSG.pytmod_extract.info, module)
            node_lst += self.__get_doc_from_module(module)
        return node_lst


if __name__ == "__main__":
    import doctest
    doctest.testmod()
