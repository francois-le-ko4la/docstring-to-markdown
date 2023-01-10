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

from pathlib import Path
from typing import NamedTuple, Union

from docstring2md.__config__ import EX_OK, EX_OSFILE, EX_IOERR, EX_CANTCREAT, \
    LOGGING_SETUP, LOGGING_MSG
from docstring2md.log import logger


class MyFile(NamedTuple):
    """This class describe a file with a NamedTuple
    @classmethod is used to init the objects correctly.

    Notes:
                The objective is to define a file with only one NamedTuple.
                The NamedTuple will be created by the set_path function to
                define the path.

    Examples:
                >>> data_file = MyFile.set_path("lorem")
                >>> data_file.status
                72
                >>> fstab = MyFile.set_path("/etc/fstab")
                >>> fstab.path.stem
                'fstab'
                >>> fstab
                MyFile(path=PosixPath('/etc/fstab'), exists=False, status=72)
                >>> fstab.absolute()
                '/etc/fstab'
                >>> # pathlib to run the test everywhere
                >>> import pathlib
                >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
                >>> lic = MyFile.set_path(f"{path}../../LICENSE")
                >>> lic.path.stem
                'LICENSE'
                >>> lic.exists
                True
                >>> result = lic.read()
                >>> result = result.split("\\n")
                >>> result[0]
                '                    GNU GENERAL PUBLIC LICENSE'
    """
    path: Union[Path, None]
    exists: bool
    status: int

    @classmethod
    def set_path(cls, path: Union[str, None]) -> MyFile:
        """ This function create the MyFile object with the file's path.
        if path = None then return None

        Args:
                    path: The file's path.

        Returns:
                    MyFile or None

        """
        if path is None:
            return cls(path=None, exists=False, status=EX_CANTCREAT)
        _exists: bool = Path(path).exists()
        _status: int = EX_OK if _exists else EX_OSFILE
        return cls(path=Path(path), exists=_exists, status=_status)

    def __repr__(self) -> str:
        _repr: str = f"path={repr(self.path)}, exists={self.exists}, status" \
                     f"={self.status}"
        return f'{self.__class__.__name__}({_repr})'

    def read(self) -> str:
        """
        read the text

        Returns:
                    str: Text if successful else ""

        """
        if self.path:
            return self.path.read_text()
        return ""

    def write(self, data: str) -> int:
        """
        Write data in the file

        Returns:
                    int: status
                    return EX_OK: 0 -> success
                    return EX_CANTCREAT: 73 -> can't create the file
                    return EX_IOERR: 74 -> write error

        """
        if not self.path:
            return EX_CANTCREAT
        try:
            with open(self.path, 'w', encoding=LOGGING_SETUP.encoding) as file:
                try:
                    file.write(data)
                except (IOError, OSError):
                    logger.error(LOGGING_MSG.io_err.error)
                    return EX_IOERR
        except (FileNotFoundError, PermissionError, OSError):
            logger.error(LOGGING_MSG.file_not_found.error)
            return EX_CANTCREAT
        logger.info(LOGGING_MSG.write_doc.info)
        return EX_OK

    def resolve(self) -> str:
        """
        get path.resolve()

        Returns:
                    str

        """
        if self.path:
            return str(self.path.resolve())
        return ""

    def absolute(self) -> str:
        """
        get path.absolute()

        Returns:
                    str

        """
        if self.path:
            return str(self.path.absolute())
        return ""


if __name__ == "__main__":
    import doctest

    doctest.testmod()
