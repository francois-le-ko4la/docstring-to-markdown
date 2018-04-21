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

import os, sys
import shlex, subprocess
from docstring2md import DocString2MD
import unittest


class TestDocstring2MD(unittest.TestCase):
    """ Unittest class to test the package
    """
    def test_cls_1_importfile(self):
        myfile = os.path.join(os.path.dirname(__file__), "/../docstring2md/docstring2md.py")
        module_pathsplit = os.path.split(myfile)
        if module_pathsplit[0] is not '':
            sys.path.append(module_pathsplit[0])
        module = DocString2MD(module_pathsplit[1].replace('.py', ''))
        self.assertTrue(module.import_module())

    def test_cls_2_importmodule(self):
        module = DocString2MD("docstring2md")
        self.assertTrue(module.import_module())

    def test_cls_3_export(self):
        module = DocString2MD("docstring2md")
        module.import_module()
        doc=module.get_doc()
        self.assertTrue(doc is not "")

    def test_script(self):
        path = os.path.dirname(__file__)+"/"
        cmd = "{0} -i {1}".format(path + "/../bin/export_docstring2md.py ",
                                        os.path.realpath(__file__),
                                        )
        args = shlex.split(cmd)
        self.assertTrue(subprocess.Popen(args))


if __name__ == '__main__':
    """if main...
    """
    unittest.main()
