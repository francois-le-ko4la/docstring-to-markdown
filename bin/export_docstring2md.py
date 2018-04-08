#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import getopt
from docstring2md import DocString2MD


def printusage():
    print('export_docstring2md.py -i <inputmodule> [-o <outputfile>]')


def main(argv):
    inputmodule = None
    outputfile = None
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["imodule=","ofile="])
    except getopt.GetoptError:
        printusage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printusage()
            sys.exit()
        elif opt in ("-i", "--imodule"):
            inputmodule = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if inputmodule is None:
        printusage()
        exit(1)

    if os.path.exists(inputmodule):
        module_pathsplit = os.path.split(inputmodule)
        if module_pathsplit[0] is not '':
            sys.path.append(module_pathsplit[0])

        module = DocString2MD(module_pathsplit[1].replace('.py',''), outputfile)
        module.import_module()
        doc=module.get_doc()
        if outputfile is None:
            print(doc)
    else:
        print("File not found !")
        exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])
