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


class PytFile(object):

    """
    >>> data_file = PytFile("lorem")
    Traceback (most recent call last):
    ...
    OSError: File not found ! lorem
    >>> data_file = PytFile(None)
    >>> data_file.exists()
    False
    >>> fstab = PytFile("/etc/fstab")
    >>> fstab.filename.stem
    'fstab'
    >>> fstab
    /etc/fstab
    >>> # pathlib to run the test everywhere
    >>> import pathlib
    >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
    >>> license = PytFile(path + "../LICENSE")
    >>> license.filename.stem
    'LICENSE'
    >>> license.exists()
    True
    >>> result = license.read()
    >>> result = result.split("\\n")
    >>> result[0]
    '                    GNU GENERAL PUBLIC LICENSE'

    """

    def __init__(self, filename, resolve=True):
        self.__filename = pathlib.Path()
        self.__exists = False
        self.__resolve = resolve
        self.filename = filename

    @property
    def filename(self):
        """
        path to the module
        """
        return self.__filename

    @filename.setter
    def filename(self, value):
        """
        Store the path
        """
        if value is None:
            return
        if pathlib.Path(str(value)).exists():
            if self.__resolve:
                self.__filename = pathlib.Path(str(value)).resolve()
            else:
                self.__filename = pathlib.Path(str(value))
        else:
            self.__exists = False
            raise IOError("File not found ! {}".format(value))
        self.__exists = True

    def exists(self):
        """
        file exists
        """
        return self.__exists

    def __repr__(self):
        return str(self.__filename)

    def __str__(self):
        return repr(self)

    def read(self):
        """
        read the text
        """
        return self.__filename.read_text()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
