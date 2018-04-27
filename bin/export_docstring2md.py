#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import sys
import argparse
from docstring2md import *


class ArgsManagement(object):

    def __init__(self, argv):
        self.parser = argparse.ArgumentParser(
            prog=pathlib.Path(__file__).name,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=docstring2md.__about__.__script_description__,
            epilog="Enjoy...",
            add_help=False
        )
        self.optional = self.parser.add_argument_group('optional arguments')
        self.optional.add_argument(
            "-h",
            "--help",
            action="help",
            help="show this help message and exit"
        )
        self.optional.add_argument(
            '-v',
            '--version',
            action='version',
            version=docstring2md.__about__.__version__
        )
        self.required = self.parser.add_argument_group('required arguments')
        self.required.add_argument(
            '-i',
            '--input',
            help='Input file name',
            required=True
        )
        self._optional = self.parser.add_argument_group('optional arguments')
        self._optional.add_argument(
            "-o",
            "--output",
            metavar='FILE',
            help="Output file"
        )
        self._optional.add_argument(
            "-t",
            "--runtime",
            metavar='FILE',
            help="Runtime file"
        )
        self._optional.add_argument(
            "-r",
            "--requirements",
            metavar='FILE',
            help="requirements.txt file"
        )
        self._optional.add_argument(
            "-uml",
            "--uml-diagramm",
            metavar='FILE',
            help="UML file (PNG)"
        )
        self._toc = self.parser.add_mutually_exclusive_group(required=False)
        self._toc.add_argument(
            '--toc',
            dest='toc',
            action='store_true',
            help="Enable the table of contents (DEFAULT)"
        )
        self._toc.add_argument(
            '--no-toc',
            dest='toc',
            action='store_false',
            help="Disable the table of contents"
        )
        self._toc.set_defaults(toc=True)
        self.args = self.parser.parse_args()

    def get(self):
        return self.args


def main(argv):
    args = ArgsManagement(argv)
    current_args = args.get()
    module = DocString2MD(
        module_name=current_args.input,
        export_file=current_args.output,
        runtime_file=current_args.runtime,
        requirements_file=current_args.requirements,
        uml_file=current_args.uml_diagramm,
        toc=current_args.toc
    )
    module.import_module()

    doc = module.get_doc()
    if current_args.output is None:
        print(doc)


if __name__ == '__main__':

    import time
    start_time = time.time()
    main(sys.argv[1:])
    print("--- %s seconds ---" % (time.time() - start_time))
