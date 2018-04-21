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
from subprocess import Popen, PIPE
import unittest


class RunPyCodeStyle(unittest.TestCase):
    def run_pycodesyle(self, current_file):
        proc = Popen('pycodestyle %s' % current_file,
                     stdout=PIPE,
                     stderr=PIPE,
                     shell=True
                     )
        out, err = proc.communicate()
        exitcode = proc.returncode
        if exitcode is not 0:
            print(out.decode('UTF-8'))
            print(err.decode('UTF-8'))
            self.assertTrue(False)
        self.assertTrue(True)


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
