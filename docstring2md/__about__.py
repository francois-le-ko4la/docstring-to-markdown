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
from email import message_from_string
from pkg_resources import get_distribution


if __name__ == "__main__":
    raise Exception("Do not start this script manually !")


META_FILES = ["METADATA", "PKG-INFO"]


def get_metafile(dist):
    for meta_file in META_FILES:
        if dist.has_metadata(meta_file):
            return meta_file
    raise Exception("Install the package...")


__pkg_name__ = __name__.split(".")[0]
META = get_metafile(get_distribution(__pkg_name__))
META = get_distribution(__pkg_name__).get_metadata(META)
META = message_from_string(META)
__version__ = META["Version"]
__email__ = META["Author-email"]
__author__ = META["Author"]
__url__ = META["Download-URL"]
__license__ = META["License"]
__description__ = META["Summary"]
__script__ = "export_docstring2md.py"
__script_descr__ = """
This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.
"""
__all__ = ["__version__", "__email__", "__author__", "__url__", "__license__"]
