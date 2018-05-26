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
import doctest
import unittest
import subprocess
from docstring2md import __about__


blacklist = ["__init__.py", "__about__.py", "__config__.py"]


def ch(current_file):
    return lambda self: self.run_doctest(current_file)


class RunDocTest(unittest.TestCase):
    def run_doctest(self, current_file):
        try:
            subprocess.run("python3 -m doctest -v " + current_file,
                           shell=True,
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)


code_folder = '../' + __about__.__pkg_name__ + '/'
path = pathlib.Path(
    pathlib.PurePath(
        pathlib.Path(__file__).resolve().parent, code_folder)
).resolve()
sys.path.append(path)

for current_file in list(path.glob('**/*.py')):
    current_file = pathlib.Path(current_file)
    print(current_file.name)
    print(current_file.name in blacklist)

    if current_file.name not in blacklist:
        setattr(
            RunDocTest,
            "test_mod_{}".format(current_file.name),
            ch(str(current_file))
        )


if __name__ == "__main__":
    unittest.main()
