#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #####  #         ###
#     # #          #
#       #          #
#       #          #
#       #          #
#     # #          #
 #####  #######   ### runner

"""

import pathlib
import argparse
from docstring2md import __about__
from docstring2md.doc2md import DocString2MD


PARSER = argparse.ArgumentParser(
    prog=pathlib.Path(__file__).name,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=__about__.__script_description__,
    epilog="Enjoy...",
    add_help=False
)
OPTIONAL = PARSER.add_argument_group('optional arguments')
OPTIONAL.add_argument(
    "-h",
    "--help",
    action="help",
    help="show this help message and exit"
)
OPTIONAL.add_argument(
    '-v',
    '--version',
    action='version',
    version=__about__.__version__
)
REQUIRED = PARSER.add_argument_group('required arguments')
REQUIRED.add_argument(
    '-i',
    '--input',
    help='Input file name',
    required=True
)
OPTIONAL = PARSER.add_argument_group('optional arguments')
OPTIONAL.add_argument(
    "-o",
    "--output",
    metavar='FILE',
    help="Output file"
)
OPTIONAL.add_argument(
    "-t",
    "--runtime",
    metavar='FILE',
    help="Runtime file"
)
OPTIONAL.add_argument(
    "-r",
    "--requirements",
    metavar='FILE',
    help="requirements.txt file"
)
OPTIONAL.add_argument(
    "-uml",
    "--uml-diagramm",
    metavar='FILE',
    help="UML file (PNG)"
)
TOC = PARSER.add_mutually_exclusive_group(required=False)
TOC.add_argument(
    '--toc',
    dest='toc',
    action='store_true',
    help="Enable the table of contents (DEFAULT)"
)
TOC.add_argument(
    '--no-toc',
    dest='toc',
    action='store_false',
    help="Disable the table of contents"
)
TOC.set_defaults(toc=True)
PRIV = PARSER.add_mutually_exclusive_group(required=False)
PRIV.add_argument(
    '--private-def',
    dest='priv',
    action='store_true',
    help="Show private objects"
)
PRIV.add_argument(
    '--no-private-def',
    dest='priv',
    action='store_false',
    help="Don't show private objects"
)
PRIV.set_defaults(priv=False)
ARGS = PARSER.parse_args()


def run():
    current_args = PARSER.parse_args()
    module = DocString2MD(
        module_name=current_args.input,
        export_file=current_args.output,
        runtime_file=current_args.runtime,
        requirements_file=current_args.requirements,
        uml_file=current_args.uml_diagramm,
        toc=current_args.toc,
        priv=current_args.priv
    )
    module.import_module()

    doc = module.get_doc()
    if current_args.output is None:
        print(doc)
