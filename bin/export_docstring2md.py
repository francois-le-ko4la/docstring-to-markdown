#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import sys
import argparse
from docstring2md import DocString2MD


class ArgsManagement(object):

    def __init__(self, argv):
        self.description = "Description"
        self.parser = argparse.ArgumentParser(
            prog=pathlib.Path(__file__).name,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=self.description,
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
            version='docstring2md 0.1'
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
        self.args = self.parser.parse_args()

    def get(self):
        return self.args


def main(argv):
    args = ArgsManagement(argv)
    current_args = args.get()
    module = DocString2MD(module_name=current_args.input,
                          export_file=current_args.output,
                          runtime_file=current_args.runtime,
                          requirements_file=current_args.requirements
                          )
    module.import_module()
    doc = module.get_doc()
    if current_args.output is None:
        print(doc)


if __name__ == '__main__':
    main(sys.argv[1:])
