#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import getopt
from docstring2md import DocString2MD

def main(argv):
    inputmodule = None
    outputfile = None
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["imodule=","ofile="])
    except getopt.GetoptError:
        print('./docstring2md.py -i <inputmodule> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('./docstring2md.py -i <inputmodule> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--imodule"):
            inputmodule = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if inputmodule is None:
        print('./docstring2md.py -i <inputmodule> -o <outputfile>')

    if os.path.exists(inputmodule):
        module_pathsplit = os.path.split(inputmodule)
        #print(module_pathsplit[1].replace('.py',''))
        #print("{0}*    {1}".format(module_pathsplit[0], module_pathsplit[1]))
        if module_pathsplit[0] is not '':
            print("Add path...")
            sys.path.append(module_pathsplit[0])

        module = DocString2MD(module_pathsplit[1].replace('.py',''))
        if module.check_module():
            module.import_module_from_spec()
            module.extract_docstring()
            print(module.get())
    else:
        print("File not found !")
        exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])
