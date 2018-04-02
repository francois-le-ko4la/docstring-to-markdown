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
import unittest


class TestDocstring2MD(unittest.TestCase):
    """ Unittest class to test the package
    """
    def test_docstring2md(self):
        """Function to validate the package
        """

        path = os.path.dirname(__file__)+"/"
        cmd = "{0} -i {1} -o {2}".format(path +"/../bin/export_docstring2md.py ",
                                        os.path.realpath(__file__),
                                        path + "README.md"
                                        )
        args = shlex.split(cmd)
        self.assertTrue(subprocess.Popen(args))

if __name__ == '__main__':
    """if main...
    """
    unittest.main()
