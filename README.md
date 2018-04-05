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
- [X] Validate features
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
### DocString2MD

````python
class DocString2MD:
````

><br />
> Class DocString2MD : export Google docstring to MD File. <br />
> <br />

#### DocString2MD.__create_doc
````python
def DocString2MD.__create_doc(self, member, member_isclass=False, class_member=False):
````
><br />
> Updates self.__output according to args provided. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   member (obj): inspect object <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   member_isclass (bool): False by default / if class -> True <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   class_member (bool): False by default / if def in class -> True <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
> <br />
#### DocString2MD.__extract_class
````python
def DocString2MD.__extract_class(self, module):
````
><br />
> Inspects classes in a module <br />
> Call self.__create_doc() & self.__extract_function() <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   module (obj): instpect object <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
> <br />
#### DocString2MD.__extract_function
````python
def DocString2MD.__extract_function(self, item, class_member=False):
````
><br />
> Inspects functions in a moddule. <br />
> Call self.__create_doc() <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   item (obj): inspect obect <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   class_member (bool): False by default / if def in class -> True <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
> <br />
#### DocString2MD.__format_docstring
````python
def DocString2MD.__format_docstring(self, docstring):
````
><br />
>  <br />
> <br />
#### DocString2MD.__getdoc
````python
def DocString2MD.__getdoc(self, obj):
````
><br />
> Call inspect.getdoc with obj parameter. <br />
> If docstring is not usable returns an empty string. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   str: docstring <br />
> <br />
#### DocString2MD.__writedoc
````python
def DocString2MD.__writedoc(self):
````
><br />
> Writes the content in the file <br />
>  <br />
> <b> args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   bool: The return value. True for success, False otherwise. <br />
> <br />
#### DocString2MD.__init__
````python
def DocString2MD.__init__(self, module_name, export_file=None):
````
><br />
> Init the ConfigFromJson Class <br />
> This function define default attributs. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   module_name (str): /path/to/the/module/ <br />
>  <br />
> <b> Attributes: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__module_name <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__module <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__module_spec <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__output <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__firstItem <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   obj <br />
> <br />
#### DocString2MD.check_module
````python
def DocString2MD.check_module(self):
````
><br />
> Checks if module can be imported without actually importing it. <br />
> Updates self.__module_spec in order to import the module. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Retuns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   bool: The return value. True for success, False otherwise. <br />
> <br />
#### DocString2MD.extract_doc
````python
def DocString2MD.extract_doc(self):
````
><br />
> <b> Extract docstring inside the module and updates self.__output: </b> <br />
> - Header <br />
> - Class <br />
> - Functions <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
> <br />
#### DocString2MD.get_doc
````python
def DocString2MD.get_doc(self):
````
><br />
> Returns self.__output <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   str: self.__output <br />
> <br />
#### DocString2MD.import_module
````python
def DocString2MD.import_module(self):
````
><br />
> Import the module via the passed in module specification <br />
> Returns the newly imported module and updates attributes self.__module <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
> <br />
