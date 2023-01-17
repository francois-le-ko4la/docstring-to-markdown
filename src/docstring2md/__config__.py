#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docstring2md: Config.

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
from __future__ import annotations

import os
from typing import NamedTuple
from enum import Enum, unique

if __name__ == "__main__":
    raise Exception("Do not start this script manually !")


@unique
class Const(Enum):
    """Define constants."""

    DOCSTRING_EMPTY: str = "Docstring empty"
    HEAD_TAG: str = "#"
    DEV_HEAD: str = "# Dev notes"
    DEV_TOML: str = "## TOML file:"
    DEV_UML: str = "## UML Diagram:"
    DEV_OBJ: str = "## Objects:"
    DECORATOR_TAG: str = '@'
    FUNCTION_TAG: str = 'def '
    PROPERTY_TAG: str = '@Property'
    COMA: str = ", "
    DOT: str = "."


@unique
class Tag(Enum):
    """Define TAG used to build MD file."""

    BEG_END_CO: str = "\n```"
    BEG_MERMAID: str = "\n```mermaid\n"
    BEG_TOML: str = "\n```toml\n"
    BEG_PY: str = "```python\n"
    BEG_PRE: str = "<pre>"
    END_PRE: str = "</pre>"
    BEG_STR: str = "^"
    END_STR: str = "$"
    END_STRH: str = ":$"
    BEG_B: str = "<b>"
    END_B: str = "</b>"
    END_BH: str = ":</b>"
    BEG_TITLE: str = "#"
    END_TITLE: str = ":"
    SPACE: str = " "
    TAB: str = "    "
    HTML_TAB: str = "&nbsp;" * 15 + "  "
    CR: str = "\n"
    HTML_CR: str = "<br />"
    QUOTE: str = "> "
    COMA: str = ", "


# logging
class LoggingSetup(NamedTuple):
    """Define logging Parameters.

    Examples:
    >>> my_setup = LoggingSetup()
    >>> my_setup.default_level
    'INFO'

    """

    logfile: str = ""
    default_level: str = 'INFO'
    default_format: str = '%(message)s'
    simple_format: str = '%(levelname)s %(message)s'
    file_format: str = '%(asctime)s - %(levelname)s - %(message)s'
    encoding: str = 'utf-8'

    @classmethod
    def set_logfile(cls, path: str) -> "LoggingSetup":
        """Define the logfile.

        This function create the LoggingSetup object with the log file's path.

        Args:
            path: The file's path.

        Returns:
            MyFile

        Examples:
            >>> a = LoggingSetup.set_logfile('report.log')
            >>> str(a)[0:32]
            "LoggingSetup(logfile='report.log"
        """
        return cls(path)


LOGGING_SETUP: LoggingSetup = LoggingSetup()


class EventMSG(NamedTuple):
    """Define Messages with different sev.

    Attributes:
        info (str): message for info ("" by default)
        warning (str): message for warning ("" by default)
        error (str): message for error ("" by default)
        debug (str): message for debug ("" by default)

    Examples:
        >>> logfile = EventMSG(info="Log file used: %s")
        >>> logfile.info
        'Log file used: %s'

    """

    info: str = ""
    warning: str = ""
    error: str = ""
    debug: str = ""


class LogMessages(NamedTuple):
    """Set standard logging messages."""

    logfile: EventMSG = EventMSG(
        info="Log file used: %s")
    args: EventMSG = EventMSG(
        debug="Arguments: %s")
    python: EventMSG = EventMSG(
        info="Python version is supported: %s",
        error="Python version is not supported: %s",
        debug="Python: %s")
    dump: EventMSG = EventMSG(
        info="New report has been created: %s",
        error="New report has not been created.",
        debug="New report cannot be saved:")
    result: EventMSG = EventMSG(
        info="Result:\n%s")
    elapse_time: EventMSG = EventMSG(
        info="Elapse time: %s s")
    pytmod: EventMSG = EventMSG(
        info="PytMod: start reading %s",
        debug="PytMod: module=%s")
    pytmod_mod: EventMSG = EventMSG(
        info="PytMod: This is a python module (%s)")
    pytmod_script: EventMSG = EventMSG(
        info="PytMod: This is a script or a folder (%s)",
        debug="PytMod: details => %s")
    pytmod_extract: EventMSG = EventMSG(
        info="PytMod - extract %s")
    new_module: EventMSG = EventMSG(
        info="PytMod - new module => %s",
        error="check your module.",
        debug="New ModuleDef - title: %s / def: %s / doc: %s / lvl: %s")
    new_class: EventMSG = EventMSG(
        debug="New ClassDef - title: %s / def: %s / doc: %s / lvl: %s")
    new_func: EventMSG = EventMSG(
        debug="New FuncDef - title: %s / def: %s / doc: %s / lvl: %s")
    node_link_analysis_beg: EventMSG = EventMSG(
        info="Node link analysis: started")
    node_link_analysis_end: EventMSG = EventMSG(
        info="Node link analysis: finished")
    unknown_type_of_node: EventMSG = EventMSG(
        warning="__get_value_from_node - another object: %s")
    io_err: EventMSG = EventMSG(
        error="Error writing to the file.")
    file_not_found: EventMSG = EventMSG(
        error="Error opening file")
    write_doc: EventMSG = EventMSG(
        info="Doc has been created")


LOG_MSG = LogMessages()

# python
CHK_PYT_MIN: tuple[int, int, int] = (3, 7, 0)
ROOT_DIR: str = os.path.abspath(os.path.dirname(__file__))
PID: int = os.getpid()


# exit values
class ExitStatus(Enum):
    """Define Exit status."""

    EX_OK: int = getattr(os, 'EX_OK', 0)
    EX_OSFILE: int = getattr(os, 'EX_OSFILE', 72)
    EX_CANTCREAT: int = getattr(os, 'EX_CANTCREAT', 73)
    EX_IOERR: int = getattr(os, 'EX_IOERR', 74)
    EX_CONFIG: int = getattr(os, 'EX_CONFIG', 78)


ARG_STYLE: dict[str, str] = {
    'argparse.yellow': 'yellow',
    'argparse.byellow': 'yellow bold',
    'argparse.cyan': 'cyan',
    'argparse.bcyan': 'cyan bold',
    'argparse.red': 'red',
    'argparse.green': 'green',
    'argparse.bgreen': 'green bold',
    'argparse.magenta': 'magenta',
    'argparse.grey': 'grey37 bold'}
ARG_HIGHLIGHT: list[str] = [
    r'(?P<cyan>INFO)',
    r'(?P<red>ERROR)',
    r'(?P<green>DEBUG)',
    r'([$]|c:\\>) (?P<red>\S+)',
    r'\n(?P<groups>[^\s](.+:))\n',
    r'(?P<green>(\"(.+?)\"))',
    r'(?P<bgreen>✔)',
    r'(?P<byellow>(Python 3|Pip3|PEP8|Pylint|Prospector))',
    r'(?P<bcyan>(MAC OS|Windows))',
    r'(?P<grey>([$]|c:\\>))',
    r'(?P<grey>((?:#|http)\S+))',
    r'(-i|-c) (?P<metavar>[a-zA-Z0-9_. ]+)',
    r'(?P<magenta>(<\S+>|\S+==\S+))',
    r'[ \(]+(?P<bcyan>[\d]+[.][\d.]+[s+]*)']
