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

import os
from typing import NamedTuple

if __name__ == "__main__":
    raise Exception("Do not start this script manually !")


class Const(NamedTuple):
    """Constants"""
    docstring_empty: str = "Docstring empty"
    head_tag: str = "#"
    dev_head: str = "# Dev notes"
    dev_toml: str = "## TOML file:"
    dev_uml: str = "## UML Diagram:"
    dev_obj: str = "## Objects:"
    decorator_tag: str = '@'
    function_tag: str = 'def '
    property_tag: str = '@Property'
    coma: str = ", "
    dot: str = "."


class Tag(NamedTuple):
    """TAG used to convert"""
    beg_co: str = "\n```\n"
    end_co: str = "\n```\n"
    beg_mermaid: str = "\n```mermaid\n"
    beg_toml: str = "\n```toml\n"
    beg_py: str = "```python\n"
    end_py: str = "\n```"
    beg_pre: str = "<pre>"
    end_pre: str = "</pre>"
    beg_str: str = "^"
    end_str: str = "$"
    end_strh: str = ":$"
    beg_b: str = "<b>"
    beg_title: str = "#"
    end_title: str = ":"
    end_b: str = "</b>"
    end_bh: str = ":</b>"
    space: str = " "
    tab: str = "    "
    html_tab: str = "&nbsp;" * 15 + "  "
    cr: str = "\n"
    html_cr: str = "<br />"
    quote: str = "> "
    coma: str = ", "


# logging
class LoggingSetup(NamedTuple):
    """Logging Parameters

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
        """ This function create the LoggingSetup object with the log file's
        path.

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


class LoggingMSG(NamedTuple):
    """
    This call define Messages with different sev.

    Attributes:
        info (str): message for info ("" by default)
        warning (str): message for warning ("" by default)
        error (str): message for error ("" by default)
        debug (str): message for debug ("" by default)


    Examples:
        >>> logfile = LoggingMSG(info="Log file used: %s")
        >>> logfile.info
        'Log file used: %s'

    """
    info: str = ""
    warning: str = ""
    error: str = ""
    debug: str = ""


class LoggingMSGCollection(NamedTuple):
    """All logging messages

    Examples:
        >>> log_msg = LoggingMSGCollection()
        >>> log_msg.logfile.info
        'Log file used: %s'

    """
    logfile: LoggingMSG = LoggingMSG(
        info="Log file used: %s")
    args: LoggingMSG = LoggingMSG(
        debug="Arguments: %s")
    python: LoggingMSG = LoggingMSG(
        info="Python version is supported: %s",
        error="Python version is not supported: %s",
        debug="Python: %s")
    dump: LoggingMSG = LoggingMSG(
        info="New report has been created: %s",
        error="New report has not been created.",
        debug="New report cannot be saved:")
    result: LoggingMSG = LoggingMSG(
        info="Result:\n%s")
    elapse_time: LoggingMSG = LoggingMSG(
        info="Elapse time: %s s")
    pytmod: LoggingMSG = LoggingMSG(
        info="PytMod: start reading %s",
        debug="PytMod: module=%s")
    pytmod_mod: LoggingMSG = LoggingMSG(
        info="PytMod: This is a python module (%s)")
    pytmod_script: LoggingMSG = LoggingMSG(
        info="PytMod: This is a script or a folder (%s)",
        debug="PytMod: details => %s")
    pytmod_extract: LoggingMSG = LoggingMSG(
        info="PytMod - extract %s")
    new_module: LoggingMSG = LoggingMSG(
        info="PytMod - new module => %s",
        error="check your module.",
        debug="New ModuleDef - title: %s / def: %s / doc: %s / lvl: %s")
    new_class: LoggingMSG = LoggingMSG(
        debug="New ClassDef - title: %s / def: %s / doc: %s / lvl: %s")
    new_func: LoggingMSG = LoggingMSG(
        debug="New FuncDef - title: %s / def: %s / doc: %s / lvl: %s")
    node_link_analysis_beg: LoggingMSG = LoggingMSG(
        info="Node link analysis: started")
    node_link_analysis_end: LoggingMSG = LoggingMSG(
        info="Node link analysis: finished")
    unknown_type_of_node: LoggingMSG = LoggingMSG(
        warning="__get_value_from_node - another object: %s")
    io_err: LoggingMSG = LoggingMSG(
        error="Error writing to the file.")
    file_not_found: LoggingMSG = LoggingMSG(
        error="Error opening file")
    write_doc: LoggingMSG = LoggingMSG(
        info="Doc has been created")


# python
CHK_PYT_MIN: tuple[int, int, int] = (3, 7, 0)
ROOT_DIR: str = os.path.abspath(os.path.dirname(__file__))
PID: int = os.getpid()
# exit values
EX_OK: int = getattr(os, 'EX_OK', 0)
EX_OSFILE: int = getattr(os, 'EX_OSFILE', 72)
EX_CANTCREAT: int = getattr(os, 'EX_CANTCREAT', 73)
EX_IOERR: int = getattr(os, 'EX_IOERR', 74)
EX_CONFIG: int = getattr(os, 'EX_CONFIG', 78)
# Const
CONST: Const = Const()
TAG: Tag = Tag()
LOGGING_SETUP: LoggingSetup = LoggingSetup()
LOGGING_MSG: LoggingMSGCollection = LoggingMSGCollection()
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
