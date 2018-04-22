#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import sys
import pathlib
import shlex
import subprocess
from docstring2md import DocString2MD
import unittest


class TestDocstring2MD(unittest.TestCase):

    """ Unittest class to test the package
    """

    def test_cls_1_importfile(self):
        path = pathlib.Path(
            pathlib.PurePath(
                pathlib.Path(__file__).resolve().parent, '../docstring2md/')
        ).resolve()
        sys.path.append(path)
        myfile = pathlib.PurePath(path, "docstring2md.py")

        module = DocString2MD(myfile.stem)
        self.assertTrue(module.import_module())

    def test_cls_2_importmodule(self):
        module = DocString2MD("docstring2md")
        self.assertTrue(module.import_module())

    def test_cls_3_export(self):
        module = DocString2MD("docstring2md")
        module.import_module()
        doc = module.get_doc()
        self.assertTrue(doc is not "")

    def test_cls_4_filenotfound(self):
        try:
            module = DocString2MD("dxocstring2md")
            self.assertTrue(module.import_module())
        except OSError as error:
            self.assertTrue(True)

    def test_cls_5_fileisnotmodule(self):
        try:
            module_name = pathlib.Path(
                pathlib.PurePath(
                    pathlib.Path(__file__).resolve().parent,
                    '../README.md'
                )
            ).resolve()
            module = DocString2MD(module_name)
            module.import_module()
        except Exception as error:
            self.assertTrue(True)

    def test_script(self):
        script = pathlib.Path(
            pathlib.PurePath(
                pathlib.Path(__file__).resolve().parent,
                '../bin/export_docstring2md.py'
            )
        ).resolve()

        cmd = "{0} -i {1}".format(script, "docstring2md")
        args = shlex.split(cmd)
        self.assertTrue(subprocess.Popen(args))


if __name__ == '__main__':
    """if main...
    """
    unittest.main()
