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


### ConvertMD()

````python
class ConvertMD():
````


> <br />
> Prepare MD string<br />
> <br />

#### ConvertMD.md_tag(begin_tag, end_tag)

````python
def ConvertMD.md_tag(begin_tag, end_tag):
````


> <br />
> Decorator - add a tag<br />
> <br />
> <b>Example:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ('__', '__') => __ TXT __<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  begin_tag (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_tag (str)<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />

#### ConvertMD.replace_beginning_and_end(begin_regexp, end_regexp, begin_tag, end_tag)

````python
def ConvertMD.replace_beginning_and_end(begin_regexp, end_regexp, begin_tag, end_tag):
````


> <br />
> Decorator - replace the beggining and the end<br />
> <br />
> <b>Example:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  All new lines must be provided with a specific tag<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  > 'Line' <br /><br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  begin_regexp (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_regexp (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  begin_tag (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_tag (str)<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />

#### ConvertMD.replace_string(old_string, new_string)

````python
def ConvertMD.replace_string(old_string, new_string):
````


> <br />
> Decorator - search & replace a string by another string<br />
> Example : replace space by a HTML tag.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  old_string (str): string to search<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  new_string (str): new string<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />

### DocString2MD()

````python
class DocString2MD():
````


> <br />
> Class DocString2MD : export Google docstring to MD File.<br />
> <br />

#### DocString2MD.__init__(self, module_name, export_file=None)

````python
def DocString2MD.__init__(self, module_name, export_file=None):
````


> <br />
> Init the class<br />
> This function define default attributs.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  module_name (str): /path/to/the/module/<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  export_file (str): /path/to/the/doc/file - None by default<br />
> <br />
> <b>Attributes:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__export_file (str): /path/to/the/doc/file - None by default<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__my_module<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__output<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  obj<br />
> <br />

#### DocString2MD.__writedoc(self)

````python
def DocString2MD.__writedoc(self):
````


> <br />
> Writes the content in the file<br />
> <br />
> <b>args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: The return value. True for success, False otherwise.<br />
> <br />

#### DocString2MD.get_doc(self)

````python
def DocString2MD.get_doc(self):
````


> <br />
> Extract the doc<br />
> Returns self.__output or self.__writedoc<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str: self.__output<br />
> <br />

#### DocString2MD.import_module(self)

````python
def DocString2MD.import_module(self):
````


> <br />
> None<br />
> <br />

### DocStringObj()

````python
class DocStringObj():
````


> <br />
> String to store and prepare the docstring.<br />
> This object will become an attribute.<br />
> <br />

#### DocStringObj.__init__(self, value)

````python
def DocStringObj.__init__(self, value):
````


> <br />
> Store the docstring<br />
> <br />

#### DocStringObj.__repr__(self)

````python
def DocStringObj.__repr__(self):
````


> <br />
> Provide the new docstring with MD tags.<br />
> <br />

#### DocStringObj.__str__(self)

````python
def DocStringObj.__str__(self):
````


> <br />
> Call repr<br />
> <br />

### ExtractPythonModule()

````python
class ExtractPythonModule():
````


> <br />
> Object in order to extract Python functions, classes....<br />
> <br />

#### ExtractPythonModule.__check_module(func)

````python
def ExtractPythonModule.__check_module(func):
````


> <br />
> Decorator - Checks if module can be imported.<br />
> Updates self.__module_spec in order to import the module.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Retuns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: The return value. True for success, False otherwise.<br />
> <br />

#### ExtractPythonModule.__extract(self, my_pythonobj, inspectmembers, level=0)

````python
def ExtractPythonModule.__extract(self, my_pythonobj, inspectmembers, level=0):
````


> <br />
> Inspects classes & functions in a moddule.<br />
> Store information in a PythonObj object.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  inspectmembers (obj): inspect obect<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  my_pythonobj (PythonObj): object to define a Python member<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />

#### ExtractPythonModule.__init__(self, module_name)

````python
def ExtractPythonModule.__init__(self, module_name):
````


> <br />
> Init<br />
> <br />

#### ExtractPythonModule.extract(self)

````python
def ExtractPythonModule.extract(self):
````


> <br />
> Defines module object and extracts all members.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />

#### ExtractPythonModule.import_module(self)

````python
def ExtractPythonModule.import_module(self):
````


> <br />
> Check module<br />
> Import the module via the passed in module specification<br />
> Returns the newly imported module and updates attributes self.__module<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: The return value. True for success, False otherwise.<br />
> <br />

### MembersObj()

````python
class MembersObj():
````


> <br />
> Dict() to store a python object's members.<br />
> This object will become an attribute.<br />
> <br />

#### MembersObj.__getitem__(self, index)

````python
def MembersObj.__getitem__(self, index):
````


> <br />
> None<br />
> <br />

#### MembersObj.__init__(self)

````python
def MembersObj.__init__(self):
````


> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />

#### MembersObj.__len__(self)

````python
def MembersObj.__len__(self):
````


> <br />
> None<br />
> <br />

#### MembersObj.__repr__(self)

````python
def MembersObj.__repr__(self):
````


> <br />
> Return repr(self).<br />
> <br />

#### MembersObj.__setitem__(self, index, value)

````python
def MembersObj.__setitem__(self, index, value):
````


> <br />
> None<br />
> <br />

#### MembersObj.__str__(self)

````python
def MembersObj.__str__(self):
````


> <br />
> Return str(self).<br />
> <br />

#### MembersObj.items(self)

````python
def MembersObj.items(self):
````


> <br />
> None<br />
> <br />

#### MembersObj.sortkeys(self)

````python
def MembersObj.sortkeys(self):
````


> <br />
> None<br />
> <br />

### ModuleObj()

````python
class ModuleObj():
````


> <br />
> Class in order to register module informations<br />
> __str__ is used to export with MD format.<br />
> <br />

#### ModuleObj.__init__(self, name, full_name, docstring, level=0)

````python
def ModuleObj.__init__(self, name, full_name, docstring, level=0):
````


> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />

#### ModuleObj.__repr__(self)

````python
def ModuleObj.__repr__(self):
````


> <br />
> Return repr(self).<br />
> <br />

#### ModuleObj.getallstr(self, member=None)

````python
def ModuleObj.getallstr(self, member=None):
````


> <br />
> None<br />
> <br />

#### PythonObj.__str__(self)

````python
def PythonObj.__str__(self):
````


> <br />
> Return str(self).<br />
> <br />

### PythonDefinitionObj()

````python
class PythonDefinitionObj():
````


> <br />
> <b>String so store and prepare the object definition:</b><br />
> Example : def function_name(*args)<br />
> This object will become an attribute.<br />
> <br />

#### PythonDefinitionObj.__init__(self, value)

````python
def PythonDefinitionObj.__init__(self, value):
````


> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />

#### PythonDefinitionObj.__repr__(self)

````python
def PythonDefinitionObj.__repr__(self):
````


> <br />
> Provide the definition string with MD tags.<br />
> <br />

#### PythonDefinitionObj.__str__(self)

````python
def PythonDefinitionObj.__str__(self):
````


> <br />
> Call repr<br />
> <br />

### PythonObj()

````python
class PythonObj():
````


> <br />
> Class in order to register object informations<br />
> __str__ is used to export with MD format.<br />
> <br />

#### PythonObj.__init__(self, name, full_name, docstring, level)

````python
def PythonObj.__init__(self, name, full_name, docstring, level):
````


> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />

#### PythonObj.__repr__(self)

````python
def PythonObj.__repr__(self):
````


> <br />
> Return repr(self).<br />
> <br />

#### PythonObj.__str__(self)

````python
def PythonObj.__str__(self):
````


> <br />
> Return str(self).<br />
> <br />

### TitleObj()

````python
class TitleObj():
````


> <br />
> String to store and prepare MD title<br />
> This object will become an attribute.<br />
> <br />

#### TitleObj.__init__(self, value, level)

````python
def TitleObj.__init__(self, value, level):
````


> <br />
> Init => store the sting in value and level (H1/H2/H3/...)<br />
> <br />

#### TitleObj.__repr__(self)

````python
def TitleObj.__repr__(self):
````


> <br />
> Provide the MD string according to the level<br />
> <br />

#### TitleObj.__str__(self)

````python
def TitleObj.__str__(self):
````


> <br />
> Return str(self).<br />
> <br />

### wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))

````python
def wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',)):
````


> <br />
> Decorator factory to apply update_wrapper() to a wrapper function<br />
> <br />
> Returns a decorator that invokes update_wrapper() with the decorated<br />
> function as the wrapper argument and the arguments to wraps() as the<br />
> remaining arguments. Default arguments are as for update_wrapper().<br />
> This is a convenience function to simplify applying partial() to<br />
> update_wrapper().<br />
> <br />