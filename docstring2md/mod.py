#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=W0105
"""

 #####    #   #   #####  #    #   ####   #####
 #    #    # #      #    ##  ##  #    #  #    #
 #    #     #       #    # ## #  #    #  #    #
 #####      #       #    #    #  #    #  #    #
 #          #       #    #    #  #    #  #    #
 #          #       #    #    #   ####   #####

"""

import pkgutil
import importlib
from docstring2md.ast_engine import ObjVisitor
from docstring2md.file import PytFile


class PytMod(object):

    """
    Object in order to extract Python functions, class....

    Use:
        >>> mod = PytMod("oups...")
        >>> mod.read()
        Traceback (most recent call last):
        ...
        ModuleNotFoundError: No module named 'oups'
        >>> mod = PytMod("json")
        >>> mod.read()
        >>> # print(mod.pkg_main_docstring)
        >>> # print(mod.docstring)
    """

    def __init__(self, module_name, priv=False):
        self.__doc = ""
        self.__module_docstring = ""
        self.__path = ""
        self.__module = module_name
        self.__priv = priv
        self.__toc = ""

    @property
    def module(self):
        """
        module name (str):
            modulename
            /path/to/the/mod
            ./path/to/the/mod
        """
        return self.__module

    @property
    def docstring(self):
        """
        returns all the docstrings.
        """
        return self.__doc

    @property
    def pkg_main_docstring(self):
        """
        PKG only.
        Returns the main docstring.
        """
        if self.ismodule():
            return ""
        return self.__get_doc_from_module(
            self.__path + "/__init__.py", module_docstring=True)

    @property
    def toc(self):
        """
        Returns the TOC
        """
        return self.__toc

    def ismodule(self):
        """
        If module name is a module file => True
        Else if the module name is a package => False
        """
        if self.module.endswith(".py"):
            return True
        return False

    def read(self):
        """
        Reads all files and store the result.
        """
        if self.ismodule():
            self.__doc = self.__get_doc_from_module(
                self.module, module_docstring=True)
        else:
            self.__doc = self.__get_doc_from_pkg(self.module)

    def __get_doc_from_module(self, module, module_docstring=False):
        source = PytFile(module)
        # tree = ast.parse(source.read())
        doc = ObjVisitor(module_docstring=module_docstring, priv=self.__priv)
        doc.visit(doc.get_tree(source.read()))
        self.__toc += doc.toc
        return doc.output

    def __get_doc_from_pkg(self, package):
        module = []
        output = ""
        package = importlib.import_module(package)
        self.__path = package.__path__[0]
        for importer, modname, ispkg in pkgutil.walk_packages(
                package.__path__):
            output += self.__get_doc_from_module(
                package.__path__[0] + "/" + modname + ".py")
        return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
