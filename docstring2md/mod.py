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
from docstring2md import ObjVisitor
from docstring2md import PytFile
from docstring2md.log import PytLog


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

    def __init__(self, module_name, priv=False, debug=False):
        self.__log = PytLog()
        self.__debug = debug
        if self.__debug:
            self.__log.set_debug()
        self.__log.debug("PytMod: init")
        self.__doc = ""
        self.__module_docstring = ""
        self.__path = None
        self.__module = module_name
        self.__priv = priv
        self.__toc = []
        self.__log.debug(
            "PytMod: module={} / priv={}".format(module_name, priv)
        )

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
            self.__log.debug("PytMod: {} is a module".format(self.module))
            return ""
        self.__log.debug("PytMod: {} is a mod =>".format(self.module))
        return self.__get_doc_from_module(
            self.__path + "/__init__.py", module_docstring=True)

    @property
    def toc(self):
        """
        Returns the TOC
        """
        return "\n".join(self.__toc)

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
        doc = ObjVisitor(
            module_docstring=module_docstring,
            priv=self.__priv,
            debug=self.__debug
        )
        doc.visit(doc.get_tree(source.read()))
        self.__toc.append(doc.toc)
        return doc.output

    def __get_module_list(self, package):
        module = []
        imp_pkg = importlib.import_module(package)
        if self.__path is None:
            self.__path = imp_pkg.__path__[0]
        for importer, modname, ispkg in pkgutil.walk_packages(
                imp_pkg.__path__):
            if ispkg:
                self.__log.info(
                    "PytMod - new module => {}.{}".format(package,  modname)
                )
                module += self.__get_module_list(package + "." + modname)
            else:
                if modname.startswith("__") is False:
                    module.append(imp_pkg.__path__[0] + "/" + modname + ".py")
        return module

    def __get_doc_from_pkg(self, package):
        output = []
        modules = self.__get_module_list(package)
        self.__log.debug("PytMod: {}".format(str(modules)))
        for module in modules:
            self.__log.debug("PytMod - extract {}".format(module))
            output.append(self.__get_doc_from_module(module))
        return "\n".join(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
