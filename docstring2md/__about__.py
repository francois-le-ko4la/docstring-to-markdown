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

import json
from pkg_resources import get_distribution


__pkg_name__ = __name__.split(".")[0]


try:
    ABOUT = json.loads(
        get_distribution(__pkg_name__).get_metadata("metadata.json")
    )
    __version__ = ABOUT["version"]
    __author__ = ABOUT["extensions"]["python.details"]["contacts"][0]["name"]
    __email__ = ABOUT["extensions"]["python.details"]["contacts"][0]["email"]
    __url__ = ABOUT["download_url"]
    __license__ = ABOUT["license"]
    __description__ = ABOUT["summary"]

except FileNotFoundError:
    try:
        PKGINFO = get_distribution(__pkg_name__).get_metadata('METADATA')
    except FileNotFoundError:
        PKGINFO = get_distribution(__pkg_name__).get_metadata('PKG-INFO')

    __version__ = get_distribution(__pkg_name__).version

    from email import message_from_string
    MSG = message_from_string(PKGINFO)
    for key, value in MSG.items():
        if key.startswith("Author-email"):
            __email__ = value
        elif key.startswith("Author"):
            __author__ = value
        elif key.startswith("Download-URL"):
            __url__ = value
        elif key.startswith("License"):
            __license__ = value
        elif key.startswith("Summary"):
            __description__ = value

__script__ = "export_docstring2md.py"
__script_descr__ = """
This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.
"""
