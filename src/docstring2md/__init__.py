#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# docstring2md
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)]()
![](./doc/pycodestyle-passing.svg)
![](./doc/pylint-passing.svg)
![](./doc/mypy-passing.svg)

## Description:

Generating documentation from code can be a tedious and time-consuming task.
By offering a simple and easy-to-use tool, this package aims to make the
process of creating documentation more efficient. It allows users to extract
useful information, such as function descriptions and input/output
specifications, directly from the source code (DocStrings). This can
save a  lot of time  and effort that would otherwise be spent manually
writing documentation. In addition, having documentation automatically
generated from code ensures that it stays up-to-date as the codebase
changes. Overall, this package provides a convenient solution for generating
high-quality documentation for Python projects.
All the installation process has been rebuilt with Makefile and pyproject.toml.

## Why ?:

We can find a lot of tools to generate docs from code but we want something
quick and easy to setup.
This tool can be used on python file or python package.

Semantic analysis and tree traversal are not really my passions ^^, but these
types of tools are still very interesting. Some time has passed since the
first version. I admit that Python had started to introduce typing but it was
not yet widespread. There have also been significant changes in the deployment
of packages, and since the script setup.py has no reason to exist. I have
therefore migrated to the TOML file and adapted the META import libraries.
It's true that I might have done this sooner, but I ran out of time and was
always using somewhat outdated versions of Python. Changes in the language are
constant. This new version is therefore a complete refresh, allowing me to be
more in line with what is currently being done in the Python ecosystem.


## Setup:
### User:

- Get the package:
```shell
git clone https://github.com/francois-le-ko4la/docstring-to-markdown.git
```
- Enter in the directory:
```shell
cd docstring-to-markdown
```
- Install with make on Linux/Unix/MacOS or use pip3 otherwise:
```shell
make install
```

### Dev:
- Get the package:
```shell
git clone https://github.com/francois-le-ko4la/docstring-to-markdown.git
```
- Enter in the directory:
```shell
cd docstring-to-markdown
```
- Create your environment with all dev prerequisites and install the package:
```shell
make venv
source venv/bin/activate
make dev
```

### Test:
This module has been tested and validated on Ubuntu.
```shell
make test
```

## Use:

Use the script:
```
Usage: export_docstring2md [-h] [--version] [--debug | --quiet]
                           [--logfile LOGFILE] [--toc] [--private-def] -p
                           PACKAGE [-o OUTPUT_FILE] [-t TOML_FILE]
                           [-mmd MERMAID_FILE]

This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.

Options:
  -h, --help            show this help message and exit
  --version             show version and exit
  --debug               print debug messages to stderr
  --quiet               print error messages to stderr
  --logfile LOGFILE     /path/to/file.log
  --toc                 Enable the table of contents
  --private-def         Enable the table of contents

Required Arguments:
  -p, --package PACKAGE
                        define the /path/to/the/package or <package_name>

Optional Arguments:
  -o, --output-file OUTPUT_FILE
                        /path/to/output/file (README.md)
  -t, --toml-file TOML_FILE
                        /path/to/runtime/file
  -mmd, --mermaid-file MERMAID_FILE
                        /path/to/mermaid/file.mmd

COMPATIBILITY:
    Python 3.7+ - https://www.python.org/

EXIT STATUS:
    This script exits 0 on success, and >0 if an error occurs:
    - EX_OK: 0 -> success
    - EX_CONFIG: 78 -> config error
    - EX_OSFILE: 72 -> module not found
    - EX_CANTCREAT: 73 -> can not create the file
    - EX_IOERR: 74 -> write error
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
- [X] Release 0.4.1
- [X] Rebuild the cli argument
- [X] Rebuild logging management and add more debug
- [X] Rebuild the package management through pyproject.toml
- [X] Rebuild the Makefile
- [X] Add-on : typing analysis
- [X] Create JSON example
- [X] Finish the typing
- [X] AST optimisation
- [X] Improve CONST
- [ ] Test
- [ ] Release 0.5.0

## License

This package is distributed under the [GPLv3 license](./LICENSE)

"""
