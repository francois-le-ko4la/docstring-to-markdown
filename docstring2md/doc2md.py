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

from docstring2md import PytFile
from docstring2md import PytMod
from docstring2md import CONST, TAG


class DocString2MD(object):

    """
    Class DocString2MD : export Google docstring to MD File.

    Use:
        >>> doc = DocString2MD("oups")
        >>> doc.import_module()
        False
        >>> doc = DocString2MD("docstring2md")
        >>> doc.import_module()
        True
        >>> result = doc.get_doc()
        >>> result = result.split("\\n")
        >>> print(result[0])
        # docstring2md
    """

    def __init__(self, module_name, export_file=None, runtime_file=None,
                 requirements_file=None, uml_file=None, toc=True, priv=False,
                 debug=False):
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
        self.__debug = debug
        self.__runtime = PytFile(runtime_file)
        self.__requirements = PytFile(requirements_file)
        self.__uml = PytFile(uml_file, resolve=False)
        self.__export_file = export_file
        self.__my_module = PytMod(module_name, priv, debug)
        self.__toc = toc
        self.__output = ""

    def import_module(self):
        """
        import all infos
        """
        try:
            self.__my_module.read()
        except Exception:
            return False

        # print(mod.pkg_main_docstring)
        # print(mod.docstring)
        self.__output = ""
        """ module / README """
        self.__output += self.__my_module.pkg_main_docstring
        """ runtime """
        if self.__runtime.exists():
            self.__output += "\n\n{}\n{}{}{}".format(
                CONST["dev_runtime"],
                TAG["beg_co"],
                self.__runtime.read(),
                TAG["end_co"]
            )
        """ requirements """
        if self.__requirements.exists():
            self.__output += "{}\n{}{}{}".format(
                CONST["dev_requirement"],
                TAG["beg_co"],
                self.__requirements.read(),
                TAG["end_co"]
            )
        """ UML """
        if self.__uml.exists:
            self.__output += "{}\n![alt text]({})\n\n".format(
                CONST["dev_uml"],
                self.__uml.filename)

        """ children """
        self.__output += "{}\n".format(CONST["dev_obj"])
        if self.__toc:
            self.__output += "{}\n".format(
                self.__my_module.toc)
        self.__output += "{}\n".format(
            self.__my_module.docstring)
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
