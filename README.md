# docstring2md
## Description:

This package Export Google DocString to Markdown from Python module.

The following files comprise the `docstring2md` package:
* `LICENSE`: The license file. `config-from-json` is released under the terms of
the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.

The package contents itself are in the config_from_json directory:
* `__ init __.py` Initialization file for the Python package.
* `docstring2md/docstring2md.py`: The code of interest.

## Setup:

    git clone https://github.com/francois-le-ko4la/docstring2md.git
    cd config-from-json
    sudo make install

## Test:

This module has been tested and validated on Ubuntu.

    sudo make test

## How to use this Class:

To be continued...

## Todo:

    - [X] Create the project
    - [X] Write code and tests
    - [ ] Test installation and requirements (setup.py and/or Makefile)
    - [X] Test code
    - [ ] Validate features
    - [ ] Write Doc/stringdoc
    - [ ] Run PEP8 validation
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

## Dev docstring
### Class DocString2MD:
Class documentation

#### Function DocString2MD.__extract_class_docstring(self, item):

```
None
```

#### Function DocString2MD.__extract_function_docstring(self, item, class_member=False):

```
zjedaé azjd ajkzd
```

#### Function DocString2MD.__generate_class_doc(self, clas):

```
None
```

#### Function DocString2MD.__generate_func_doc(self, func, class_member=False):

```
None
```

#### Function DocString2MD.__init__(self, module_name):

```
        
```

#### Function DocString2MD.check_module(self):

```
Checks if module can be imported without actually
importing it
```

#### Function DocString2MD.extract_docstring(self):

```
extract all
```

#### Function DocString2MD.get(self):

```
None
```

#### Function DocString2MD.import_module_from_spec(self):

```
Import the module via the passed in module specification
Returns the newly imported module
```

### Function main(argv):

```
None
```


