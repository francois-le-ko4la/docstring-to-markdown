#!/usr/bin/env python3
import os
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


path = os.path.dirname(__file__) + "/../docstring2md/"
for current_file in os.listdir(path):
    if current_file.endswith(".py"):
        def ch(current_file):
            return lambda self: self.run_pycodesyle(current_file)
        setattr(RunPyCodeStyle,
                "test_{}".format(current_file),
                ch(path + current_file)
                )


if __name__ == "__main__":
    unittest.main()
