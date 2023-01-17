#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docstring2md: log.

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
from __future__ import annotations

import logging
import os

from rich.logging import RichHandler

from docstring2md.__config__ import LOG_MSG, LOGGING_SETUP

if __name__ == "__main__":
    raise Exception("Do not start this script manually !")

# ------------------------------------------------------------------------------
# Windows specific
# ------------------------------------------------------------------------------
# enables ansi escape characters in Windows terminals
if os.name == "nt":
    os.system("")

# ------------------------------------------------------------------------------
# logging : basic config
# ------------------------------------------------------------------------------
logging.basicConfig(
    level=LOGGING_SETUP.default_level,
    format=LOGGING_SETUP.default_format,
    handlers=[RichHandler(rich_tracebacks=True, show_time=False)]
)

logger: logging.Logger = logging.getLogger(__name__)


# ------------------------------------------------------------------------------
# logging : add file
# ------------------------------------------------------------------------------

def define_logfile(path: str) -> None:
    """Define the logfile.

    This function set up the log to push log events in the report file.

    Args:
        path:str    /path/to/logfile
    Returns:
        None

    """
    log_formatter = logging.Formatter(LOGGING_SETUP.file_format)
    file_handler = logging.FileHandler(path)
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)
    logger.info(LOG_MSG.logfile.info, path)
