#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docstring2md: cli.

This script is provided by docstring2md package.

Export google docstrings from python module to a Markdown file in order to
generate README.
"""
from __future__ import annotations

import argparse
import logging
import sys
import textwrap

from rich_argparse import RawDescriptionRichHelpFormatter

from docstring2md.__about__ import (__script_descr__, __script_epilog__,
                                    __version__)
from docstring2md.__config__ import (ARG_HIGHLIGHT, ARG_STYLE, CHK_PYT_MIN,
                                     LOG_MSG, Const, ExitStatus)
from docstring2md.doc2md import DocString2MD, DocString2MDOptions
from docstring2md.file import MyFile
from docstring2md.log import define_logfile, logger


# ------------------------------------------------------------------------------
# check python
# ------------------------------------------------------------------------------
def check_python() -> bool:
    """Check python version.

    This function check Python version, log the result and return a status
    True/False.

    Returns:
        True if successful, False otherwise.

    """
    # Python __version__
    current_version: tuple[int, int, int] = sys.version_info[:3]
    if current_version < CHK_PYT_MIN:
        logger.error(
            LOG_MSG.python.error,
            Const.DOT.value.join(map(str, current_version)))
        return False
    logger.info(
        LOG_MSG.python.info,
        Const.DOT.value.join(map(str, current_version)))
    logger.debug(LOG_MSG.python.debug, sys.version)
    return True


# ------------------------------------------------------------------------------
# arguments and options
# ------------------------------------------------------------------------------
def get_argparser() -> argparse.ArgumentParser:
    """Define the argument parser.

    This function define the argument parser and return it.

    Returns:
        ArgumentParser

    Examples:
        >>> a = get_argparser()
        >>> type(a)
        <class 'argparse.ArgumentParser'>
    """
    RawDescriptionRichHelpFormatter.styles.update(ARG_STYLE)
    RawDescriptionRichHelpFormatter.highlights.extend(ARG_HIGHLIGHT)

    version: str = f'%(prog)s {__version__}'
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=__script_descr__,
        epilog=__script_epilog__,
        formatter_class=RawDescriptionRichHelpFormatter)
    parser.add_argument(
        '--version',
        help="show version and exit",
        action='version', version=version)
    exclusive_group = parser.add_mutually_exclusive_group(required=False)
    exclusive_group.add_argument(
        '--debug',
        help='print debug messages to stderr',
        default=False, action='store_true')
    exclusive_group.add_argument(
        '--quiet',
        help='print error messages to stderr',
        default=False, action='store_true')
    parser.add_argument(
        '--logfile',
        help='/path/to/file.log')
    parser.add_argument(
        '--toc',
        help='Enable the table of contents',
        default=False, action='store_true')
    parser.add_argument(
        '--private-def',
        help='Enable the table of contents',
        default=False, action='store_true')
    # New groups
    required_argument = parser.add_argument_group(
        'required arguments')
    optional_argument = parser.add_argument_group(
        'optional arguments')
    required_argument.add_argument(
        '-p', '--package',
        help=textwrap.dedent('''
        define the /path/to/the/package or <package_name>
        '''),
        required=True)
    optional_argument.add_argument(
        '-o', '--output-file',
        help=textwrap.dedent('''\
        /path/to/output/file (README.md)
        '''))
    optional_argument.add_argument(
        '-tml', '--toml-file',
        help=textwrap.dedent('''\
        /path/to/toml/file.toml
        '''))
    optional_argument.add_argument(
        '-td', '--todo-file',
        help=textwrap.dedent('''\
        /path/to/todo/file.md
        '''))
    optional_argument.add_argument(
        '-mmd', '--mermaid-file',
        help=textwrap.dedent('''\
        /path/to/mermaid/file.mmd
        '''))

    return parser


def run() -> ExitStatus:
    """Manage options and analyse modules.

    Called by the CLI runner, manage options to analyse the module.
    It exits 0 on success, and >0 if an error occurs.

    Returns:
        int: status
        return EX_OK: 0 -> success
        return EX_CONFIG: 78 -> config error
        return EX_OSFILE: 72 -> Module not found
        return EX_CANTCREAT: 73 -> can't create the file
        return EX_IOERR: 74 -> write error
    """
    parser: argparse.ArgumentParser = get_argparser()
    args: argparse.Namespace = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
    if args.quiet:
        logger.setLevel(logging.ERROR)
    if args.logfile:
        define_logfile(args.logfile)
    if not check_python():
        return ExitStatus.EX_CONFIG

    module_name: str = args.package
    options: DocString2MDOptions = DocString2MDOptions(
        toml=MyFile.set_path(args.toml_file),
        uml=MyFile.set_path(args.mermaid_file),
        todo=MyFile.set_path(args.todo_file),
        output=MyFile.set_path(args.output_file),
        toc=args.toc,
        private_def=args.private_def
    )
    module: DocString2MD = DocString2MD(module_name, options)
    status: ExitStatus = module.import_module()
    if status is not ExitStatus.EX_OK:
        logger.error(LOG_MSG.new_module.error)
        return status
    return module.writedoc()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
