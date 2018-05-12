#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 ######     #    #       ######
 #          #    #       #
 #####      #    #       #####
 #          #    #       #
 #          #    #       #
 #          #    ######  ######

"""

import pathlib
import os


class PytFile(object):

    """
    >>> fstab = PytFile("/etc/fstab")
    >>> print(fstab.filename.stem)
    fstab
    >>> print(fstab)
    /etc/fstab
    >>> # pathlib to run the test everywhere
    >>> import pathlib
    >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
    >>> license = PytFile(path + "../LICENSE")
    >>> print(license.filename.stem)
    LICENSE
    >>> #print(license.read())

    """

    def __init__(self, filename):
        self.__isdefined = False
        if filename is not None:
            self.filename = str(filename)

    @property
    def filename(self):
        return self.__path

    @filename.setter
    def filename(self, value):
        self.__path = pathlib.Path()
        if pathlib.Path(value).exists():
            self.__path = pathlib.Path(value).resolve()
        else:
            print("filename: " + value)
            raise IOError("File not found !")
        self.__isdefined = True

    @property
    def isdefined(self):
        return self.__isdefined

    def __repr__(self):
        return str(self.__path)

    def __str__(self):
        return repr(self)

    def read(self):
        return self.filename.read_text()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
