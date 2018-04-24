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
* `docstring2md/docstring2md.py`: The code of interest.

The script is in the `bin` directory:
* `export_docstring2md.py`: The script to run

## Setup:
```shell
git clone https://github.com/francois-le-ko4la/docstring2md.git
cd config-from-json
make install
```

## Test:

This module has been tested and validated on Ubuntu.
```shell
make test
```

## Use:
Use the script:
```shell
export_docstring2md.py -i <inputmodule> [-o <outputfile>]`
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

__version__ = '0.1_dev'

from .docstring2md import *
