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

from typing import NamedTuple

from docstring2md.__config__ import CONST, TAG, EX_OK, EX_OSFILE
from docstring2md.file import MyFile
from docstring2md.mod import PytMod


class DocString2MDOptions(NamedTuple):
    """
    This NamedTuple organizes all options with one NamedTuple
        export_file (str): /path/to/doc/file - None by default
        runtime_file (str): /path/to/runtime/file - None by default
        requirements_file (str): /path/to/requiremnt/file - None by default
        uml_file (str): /path/to/uml/file - None by default
        toc (bool): True -> get a table of content
        priv (bool): True -> get private function

    """
    toml: MyFile
    uml: MyFile
    export_file: MyFile
    toc: bool
    private_def: bool


class DocString2MD:

    """
    Class DocString2MD : export Google docstring to MD File.

    Examples:
                >>> options: DocString2MDOptions = DocString2MDOptions(\
                            toml=MyFile.set_path(None),\
                            uml=MyFile.set_path(None),\
                            export_file=MyFile.set_path(None),\
                            toc=False,\
                            private_def=False)
                >>> doc = DocString2MD("oups", options)
                >>> doc.import_module()
                72
                >>> doc = DocString2MD("docstring2md", options)
                >>> doc.import_module()
                0
                >>> result = doc.get_doc()
                >>> result = result.split("\\n")
                >>> print(result[0])
                # docstring2md
    """
    __options: DocString2MDOptions
    __my_module: PytMod
    __output: str = ""

    def __init__(self, module_name: str, options: DocString2MDOptions) -> None:
        """Init the class
        This function define default attributs.

        Args:
                    module_name (str): /path/to/module/ or <module_name>

        """
        self.__options = options
        self.__my_module = PytMod(module_name, options.private_def)

    def import_module(self) -> int:
        """
        Import the module.
        It exits 0 on success, and >0 if an error occurs.

        Returns:
                    int: status
                    return EX_OK: 0 -> success
                    return EX_OSFILE: 72 -> Module not found

        """
        try:
            self.__my_module.read()
        except ModuleNotFoundError:
            return EX_OSFILE

        # module / README
        _output: list = []
        if self.__my_module.pkg_main_docstring[0]:
            _output.append(self.__my_module.pkg_main_docstring[0].docstring)

        _output.extend([CONST.dev_head])
        # TOML
        if (self.__options.toml.path and
                self.__options.toml.exists):
            _output.extend([CONST.dev_toml, TAG.beg_co,
                            self.__options.toml.read(), TAG.end_co])
        # UML
        if self.__options.uml.path and self.__options.uml.exists:
            _output.extend([CONST.dev_uml, TAG.beg_mermaid,
                            self.__options.uml.read(), TAG.end_co])

        # children
        _output.append(f"{CONST.dev_obj}\n")
        if self.__options.toc:
            _output.extend([elem.get_toc_elem() for elem in
                            self.__my_module.node_lst if elem is not None])

        _output.extend([elem.get_summary() for elem in
                        self.__my_module.node_lst if elem is not None])

        self.__output = "\n".join(_output)
        return EX_OK

    def get_doc(self) -> str:
        """Returns the documentation

        Returns:
                    str: doc

        """
        return self.__output

    def writedoc(self) -> int:
        """
        Writes the doc: screen or files.
        It exits 0 on success, and >0 if an error occurs.

        args:
                    None

        Returns:
                    int: status
                    return EX_OK: 0 -> success
                    return EX_CANTCREAT: 73 -> can't create the file
                    return EX_IOERR: 74 -> write error

        """
        if self.__options.export_file:
            return self.__options.export_file.write(self.__output)
        print(self.__output)
        return EX_OK


if __name__ == "__main__":
    import doctest
    doctest.testmod()
