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
* `__ init __.py` Initialization file for the Python package.
* `docstring2md/docstring2md.py`: The code of interest.

The script is in the `bin` directory:
* `export_docstring2md.py`: The script to run

## Setup:
````shell
git clone https://github.com/francois-le-ko4la/docstring2md.git
cd config-from-json
make install
````

## Test:

This module has been tested and validated on Ubuntu.
````shell
make test
````

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
Class DocString2MD : export Google docstring to MD File.

#### Function DocString2MD.__create_doc(self, member, member_isclass=False, class_member=False):

```
Updates self.__output according to args provided.

Args:
    member (obj): inspect object
    member_isclass (bool): False by default / if class -> True
    class_member (bool): False by default / if def in class -> True

Returns:
    None
```

#### Function DocString2MD.__extract_class(self, module):

```
Inspects classes in a module
Call self.__create_doc() & self.__extract_function()

Args:
    module (obj): instpect object

Returns:
    None
```

#### Function DocString2MD.__extract_function(self, item, class_member=False):

```
Inspects functions in a moddule.
Call self.__create_doc()

Args:
    itms (obj): inspect obect
    class_member (bool): False by default / if def in class -> True

Returns:
    None
```

#### Function DocString2MD.__getdoc(self, obj):

```
Call inspect.getdoc with obj parameter.
If docstring is not usable returns an empty string.

Args:
    None

Returns:
    str: docstring
```

#### Function DocString2MD.__writedoc(self):

```
Writes the content in the file

args:
    None

Returns:
    bool: The return value. True for success, False otherwise.
```

#### Function DocString2MD.__init__(self, module_name, export_file=None):

```
Init the ConfigFromJson Class
This function define default attributs.

Args:
    module_name (str): /path/to/the/module/

Attributes:
    self.__module_name
    self.__module
    self.__module_spec
    self.__output
    self.__firstItem

Returns:
    obj
```

#### Function DocString2MD.check_module(self):

```
Checks if module can be imported without actually importing it.
Updates self.__module_spec in order to import the module.

Args:
    None

Retuns:
    bool: The return value. True for success, False otherwise.
```

#### Function DocString2MD.extract_doc(self):

```
Extract docstring inside the module and updates self.__output:
- Header
- Class
- Functions

Args:
    None

Returns:
    None
```

#### Function DocString2MD.get_doc(self):

```
Returns self.__output

Args:
    None

Returns:
    str: self.__output
```

#### Function DocString2MD.import_module(self):

```
Import the module via the passed in module specification
Returns the newly imported module and updates attributes self.__module

Args:
    None

Returns:
    None
```

