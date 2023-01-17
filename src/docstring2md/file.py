#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docstring2md: file.

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
from typing import NamedTuple, Optional

from docstring2md.__config__ import LOG_MSG, LOGGING_SETUP, ExitStatus
from docstring2md.log import logger


class MyFile(NamedTuple):
    r"""Describe a file with a NamedTuple.

    @classmethod is used to init the objects correctly.

    Notes:
        The objective is to define a file with only one NamedTuple.
        The NamedTuple will be created by the set_path function to
        define the path.

    Examples:
        >>> data_file = MyFile.set_path("lorem")
        >>> data_file.status
        <ExitStatus.EX_OSFILE: 72>
        >>> fstab = MyFile.set_path("/etc/fstab")
        >>> fstab.path.stem
        'fstab'
        >>> fstab
        MyFile(path=PosixPath(...), exists=False, status=72)
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
        >>> result = result.split("\n")
        >>> result[0]
        '                    GNU GENERAL PUBLIC LICENSE'
    """

    path: Optional[Path]
    exists: bool
    status: ExitStatus

    @classmethod
    def set_path(cls, path: Optional[str]) -> MyFile:
        """Set path and create the object.

        if path is None        -> status = ExitStatus.EX_CANTCREAT
        if path exists         -> status = ExitStatus.EX_OK
        If path does not exist -> status = ExitStatus.EX_OSFILE

        Args:
            path: The file's path.

        Returns:
            MyFile or None

        """
        if path is None:
            return cls(path=None, exists=False, status=ExitStatus.EX_CANTCREAT)
        _exists: bool = Path(path).exists()
        _status: ExitStatus = ExitStatus.EX_OK if _exists else \
            ExitStatus.EX_OSFILE
        return cls(path=Path(path), exists=_exists, status=_status)

    def __repr__(self) -> str:
        """Get the repr."""
        _repr: str = f"path={repr(self.path)}, exists={self.exists}, status" \
                     f"={self.status}"
        return f'{self.__class__.__name__}({_repr})'

    def read(self) -> str:
        """Read the file.

        Returns:
            str: Text if successful else ""

        """
        return self.path.read_text() if self.path else ""

    def write(self, data: str) -> ExitStatus:
        """Write data in the file.

        Returns:
            int: status
            return EX_OK: 0 -> success
            return EX_CANTCREAT: 73 -> can't create the file
            return EX_IOERR: 74 -> write error

        """
        if not self.path:
            return ExitStatus.EX_CANTCREAT
        try:
            with open(self.path, 'w', encoding=LOGGING_SETUP.encoding) as file:
                try:
                    file.write(data)
                except (IOError, OSError):
                    logger.error(LOG_MSG.io_err.error)
                    return ExitStatus.EX_IOERR
        except (FileNotFoundError, PermissionError, OSError):
            logger.error(LOG_MSG.file_not_found.error)
            return ExitStatus.EX_CANTCREAT
        logger.info(LOG_MSG.write_doc.info)
        return ExitStatus.EX_OK

    def resolve(self) -> str:
        """Get the resolved path.

        Returns:
            str

        """
        return str(self.path.resolve()) if self.path else ""

    def absolute(self) -> str:
        """Get the absolute path.

        Returns:
            str

        """
        if self.path:
            return str(self.path.absolute())
        return ""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
