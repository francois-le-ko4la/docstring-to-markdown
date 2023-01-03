#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Error on __version__:
# mypy: disable-error-code=attr-defined
"""
This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.
"""
from __future__ import annotations

import argparse
import logging
import sys
import textwrap

from rich_argparse import RawDescriptionRichHelpFormatter

from docstring2md.__about__ import __version__, __script_descr__, \
    __script_epilog__
from docstring2md.__config__ import CHK_PYT_MIN, LOGGING_MSG, ARG_STYLE, \
    ARG_HIGHLIGHT, EX_CONFIG, EX_OK
from docstring2md.doc2md import DocString2MD, DocString2MDOptions
from docstring2md.log import logger, define_logfile
from docstring2md.file import MyFile


# ------------------------------------------------------------------------------
# check python
# ------------------------------------------------------------------------------
def check_python() -> bool:
    """This function check Python version, log the result and return a status
    True/False.

    Returns:
        True if successful, False otherwise.

    """
    # Python __version__
    current_version: tuple = sys.version_info[:3]
    if current_version < CHK_PYT_MIN:
        logger.error(
            LOGGING_MSG.python.error, ".".join(map(str, current_version)))
        return False
    logger.info(
        LOGGING_MSG.python.info, ".".join(map(str, current_version)))
    logger.debug(LOGGING_MSG.python.debug, sys.version)
    return True


# ------------------------------------------------------------------------------
# arguments and options
# ------------------------------------------------------------------------------
def get_argparser() -> argparse.ArgumentParser:
    """
    This function describe the argument parser and return it.

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
    parser.add_argument('--version', action='version', version=version)
    exclusive_group: argparse._MutuallyExclusiveGroup = \
        parser.add_mutually_exclusive_group(required=False)
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
    required_argument: argparse._ArgumentGroup = parser.add_argument_group(
        'required arguments')
    optional_argument: argparse._ArgumentGroup = parser.add_argument_group(
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
        '-t', '--toml-file',
        help=textwrap.dedent('''\
        /path/to/runtime/file
        '''))
    optional_argument.add_argument(
        '-mmd', '--mermaid-file',
        help=textwrap.dedent('''\
        /path/to/mermaid/file.mmd
        '''))

    return parser


def run() -> int:
    """
    This function is called by the CLI runner and manage options.

    Args:
        None.

    Returns:
        print screen|file
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
        return EX_CONFIG

    module_name: str = args.package
    options: DocString2MDOptions = DocString2MDOptions(
        toml=MyFile.set_path(args.toml_file),
        uml=MyFile.set_path(args.mermaid_file),
        export_file=MyFile.set_path(args.output_file),
        toc=args.toc,
        private_def=args.private_def
    )
    module: DocString2MD = DocString2MD(module_name, options)
    status: int = module.import_module()
    if status is not EX_OK:
        logger.error("check your module.")
        return status
    return module.writedoc()
