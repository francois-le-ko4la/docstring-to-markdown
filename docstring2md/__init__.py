#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# docstring2md
## Description:

This package Export Google DocString to Markdown from Python module.

## Why ?:

We can find a lot of tools to generate docs from code but we want something
quick and easy to setup.
This tool can be used on python file or python package.

## Setup:
```shell
$ git clone https://github.com/francois-le-ko4la/docstring-to-markdown.git
$ cd docstring-to-markdown
$ make install
```

## Test:

This module has been tested and validated on Ubuntu 17.10/18.04.
```shell
$ make test
```

## Use:

Use the script:
```shell
$ export_docstring2md.py -h
usage: main.py [-h] [-v] -i INPUT [-o FILE] [-t FILE] [-r FILE] [-uml FILE]
               [--toc | --no-toc] [--private-def | --no-private-def]

This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.

optional arguments:
  --toc                 Enable the table of contents (DEFAULT)
  --no-toc              Disable the table of contents
  --private-def         Show private objects
  --no-private-def      Don't show private objects

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

required arguments:
  -i INPUT, --input INPUT
                        Input file name

optional arguments:
  -o FILE, --output FILE
                        Output file
  -t FILE, --runtime FILE
                        Runtime file
  -r FILE, --requirements FILE
                        requirements.txt file
  -uml FILE, --uml-diagramm FILE
                        UML file (PNG)

Enjoy...
```

## Project structure

```
.
├── bin
│   └── export_docstring2md.py
├── docstring2md
│   ├── __about__.py
│   ├── ast_engine.py
│   ├── __config__.py
│   ├── convmd.py
│   ├── doc2md.py
│   ├── file.py
│   ├── __init__.py
│   ├── main.py
│   └── mod.py
├── last_check.log
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pictures
│   ├── classes_docstring2md.png
│   └── packages_docstring2md.png
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.cfg
├── setup.py
└── tests
    ├── test_docstring2md.py
    ├── test_doctest.py
    └── test_pycodestyle.py
```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Add-on : decorator
- [X] Add-on : class properties
- [X] Add-on : runtime & requirements
- [X] Add-on : toc
- [X] Add-on : remove inspect library and use AST
- [X] Add-on : improve global performance (x3)
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
- [X] Release

## License

This package is distributed under the [GPLv3 license](./LICENSE)

"""

from docstring2md import __about__
from docstring2md.__config__ import CONST, TAG, BLACKLIST
from docstring2md.convmd import ConvMD
from docstring2md.file import PytFile
from docstring2md.ast_engine import ObjVisitor
from docstring2md.mod import PytMod
from docstring2md.doc2md import DocString2MD


__version__ = __about__.__version__
__author__ = __about__.__author__
__license__ = __about__.__license__
