#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# docstring2md
## Description:

This package Export Google DocString to Markdown from Python module.

The following files comprise the `docstring2md` package:
* `LICENSE`: The license file. `docstring2md` is released under the terms of
the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.

The package contents itself are in the `docstring2md` directory:
* `__init__.py` Initialization file for the Python package.
* `__about__.py` Global parameters
* `doc2md.py`: The code of interest.

The script is in the `bin` directory:
* `export_docstring2md.py`: The script to run

## Setup:
```shell
git clone https://github.com/francois-le-ko4la/docstring-to-markdown.git
cd docstring-to-markdown
make install
```

## Test:

This module has been tested and validated on Ubuntu 17.10/18.04.
```shell
make test
```

## Use:

Use the script:
```shell
$ export_docstring2md.py -h
usage: export_docstring2md.py [-h] [-v] -i INPUT [-o FILE] [-t FILE] [-r FILE]
                              [-uml FILE] [--toc | --no-toc]

This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.

optional arguments:
  --toc                 Enable the table of contents (DEFAULT)
  --no-toc              Disable the table of contents

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
- [ ] Write Doc/stringdoc
- [X] Run PEP8 validation
- [ ] Clean & last check
- [ ] Release

## Note:
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import docstring2md.__about__
from docstring2md.doc2md import *
