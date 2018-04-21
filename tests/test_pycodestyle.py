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

import pathlib
import pycodestyle
import unittest


class RunPyCodeStyle(unittest.TestCase):
    def run_pycodesyle(self, current_file):

        style = pycodestyle.StyleGuide()
        result = style.check_files([current_file])
        self.assertEqual(result.total_errors, 0),


path = pathlib.Path(
                    pathlib.PurePath(
                            pathlib.Path(__file__).resolve().parent, '../')
                    ).resolve()
for current_file in list(path.glob('**/*.py')):
    def ch(current_file):
        return lambda self: self.run_pycodesyle(current_file)
    setattr(RunPyCodeStyle,
            "test_{}".format(current_file),
            ch(current_file)
            )


if __name__ == "__main__":
    unittest.main()
