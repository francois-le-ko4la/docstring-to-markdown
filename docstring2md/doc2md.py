#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=W0105
"""

                         #####
 #####    ####    ####  #     #  #    #  #####
 #    #  #    #  #    #       #  ##  ##  #    #
 #    #  #    #  #       #####   # ## #  #    #
 #    #  #    #  #      #        #    #  #    #
 #    #  #    #  #    # #        #    #  #    #
 #####    ####    ####  #######  #    #  #####


"""

import pathlib
import sys
from docstring2md.file import PytFile
from docstring2md.module import ExtractPythonModule
from docstring2md.__config__ import MyConst, Tag


class DocString2MD(object):

    """
    Class DocString2MD : export Google docstring to MD File.

    Use:
        >>> doc = DocString2MD("docstring2md")
        >>> doc.import_module()
        True
        >>> result = doc.get_doc()
        >>> result = result.split("\\n")
        >>> print(result[0])
        # docstring2md
    """

    def __init__(self, module_name, export_file=None, runtime_file=None,
                 requirements_file=None, uml_file=None, toc=True, priv=False):
        """Init the class
        This function define default attributs.

        Args:
            module_name (str): /path/to/the/module/
            export_file (str): /path/to/the/doc/file - None by default

        Attributes:
            self.__export_file (str): /path/to/the/doc/file - None by default
            self.__my_module
            self.__output

        Returns:
            obj

        """
        self.__runtime = PytFile(runtime_file)
        self.__requirements = PytFile(requirements_file)
        self.__uml = PytFile(uml_file)
        self.__export_file = export_file
        self.module_name = module_name
        self.__my_module = ExtractPythonModule(self.module_name, priv)
        self.__toc = toc
        self.__output = ""

    @property
    def module_name(self):
        """
        return /path/to/the/json/file

        Args:
            None

        Returns:
            None

        """
        return self.__module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        check the path to the module
        Store the path

        Args:
            module_name(str): /path/to/the/module

        Returns:
            None
        """
        module_name = pathlib.Path(module_name).resolve()
        if pathlib.Path(module_name).exists():
            sys.path.append(module_name.parents[0])
            self.__module_name = module_name.stem
        else:
            raise IOError("Module not found ! ({})".format(module_name))

    def import_module(self):
        """
        import all infos
        """
        if self.__my_module.import_module():
            self.__my_module.extract()
            self.__output = ""
            """ module / README """
            self.__output += str(self.__my_module.module)
            """ runtime """
            if self.__runtime.exists():
                self.__output += "{}\n{}{}{}".format(
                    MyConst.dev_runtime,
                    Tag.beg_co,
                    self.__runtime.read(),
                    Tag.end_co
                )
            """ requirements """
            if self.__requirements.exists():
                self.__output += "{}\n{}{}{}".format(
                    MyConst.dev_requirement,
                    Tag.beg_co,
                    self.__requirements.read(),
                    Tag.end_co
                )
            """ UML """
            if self.__uml.exists:
                self.__output += "{}\n![alt text]({})\n\n".format(
                    MyConst.dev_uml,
                    self.__uml.filename)

            """ children """
            self.__output += "{}\n".format(MyConst.dev_obj)

            if self.__toc:
                self.__output += "{}\n".format(
                    self.__my_module.module.gettoc())

            self.__output += "{}\n".format(
                self.__my_module.module.getallstr())
            return True
        else:
            return False

    def get_doc(self):
        """

        Extract the doc
        Returns self.__output or self.__writedoc

        Args:
            None

        Returns:
            str: self.__output
        """

        if self.__export_file is None:
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
            export_file = open(self.__export_file, "w")
            try:
                export_file.write(self.__output)
            finally:
                export_file.close()
        except IOError:
            print("Unable to create {0} on disk.".format(self.__export_file))
            return False

        return True
