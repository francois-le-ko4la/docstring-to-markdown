#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Metadata with importlib_metadata:
# mypy: disable-error-code=no-redef
"""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.
This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata  # type: ignore

if __name__ == "__main__":
    raise Exception("Do not start this script manually !")

__pkg_name__: str = "docstring2md"
__version__: str = metadata.version(__pkg_name__)
__author__: str = metadata.metadata(__pkg_name__)["Author"]
__url__: str = metadata.metadata(__pkg_name__)["Project-URL"]
__license__: str = metadata.metadata(__pkg_name__)["License"]
__description__: str = metadata.metadata(__pkg_name__)["Summary"]
__script__: str = "export_docstring2md"
__script_descr__: str = """
This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.
"""
__script_epilog__: str = """
COMPATIBILITY:
    Python 3.7+ - https://www.python.org/
EXIT STATUS:
    This script exits 0 on success, and >0 if an error occurs:
    - EX_OK: 0 -> success
    - EX_CONFIG: 78 -> config error
    - EX_OSFILE: 72 -> module not found
    - EX_CANTCREAT: 73 -> can not create the file
    - EX_IOERR: 74 -> write error
"""
