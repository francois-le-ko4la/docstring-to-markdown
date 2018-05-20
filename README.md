# docstring2md
## Description:

This package Export Google DocString to Markdown from Python module.

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
│   ├── __config__.py
│   ├── convmd.py
│   ├── doc2md.py
│   ├── file.py
│   ├── __init__.py
│   ├── main.py
│   ├── module.py
│   └── objdef.py
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
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
- [X] Release

## License

This package is distributed under the [GPLv3 license](./LICENSE)
## Dev notes
### Runtime

```
python-3.6.x

```
### Requirements

```
setuptools>=36.2.7
pycodestyle>=2.3.1

```
### UML Diagram
![alt text](pictures/classes_docstring2md.png)

### Objects
[ConvMD()](#convmd)<br />
[ConvMD.add_tag(begin_tag, end_tag)](#convmdadd_tagbegin_tag-end_tag)<br />
[ConvMD.repl_beg_end(begin_regexp, end_regexp, begin_tag, end_tag)](#convmdrepl_beg_endbegin_regexp-end_regexp-begin_tag-end_tag)<br />
[ConvMD.repl_str(old_string, new_string)](#convmdrepl_strold_string-new_string)<br />
[DocString2MD()](#docstring2md)<br />
[@Property: DocString2MD.module_name](#property-docstring2mdmodule_name)<br />
[DocString2MD.get_doc(self)](#docstring2mdget_docself)<br />
[DocString2MD.import_module(self)](#docstring2mdimport_moduleself)<br />
[DocStringObj()](#docstringobj)<br />
[@Property: DocStringObj.value](#property-docstringobjvalue)<br />
[ExtractPythonModule()](#extractpythonmodule)<br />
[ExtractPythonModule.extract(self)](#extractpythonmoduleextractself)<br />
[ExtractPythonModule.import_module(self)](#extractpythonmoduleimport_moduleself)<br />
[MembersObj()](#membersobj)<br />
[MembersObj.items(self)](#membersobjitemsself)<br />
[MembersObj.sortkeys(self)](#membersobjsortkeysself)<br />
[ModuleObj()](#moduleobj)<br />
[ModuleObj.getallstr(self, member=None)](#moduleobjgetallstrself-membernone)<br />
[ModuleObj.gettoc(self, member=None)](#moduleobjgettocself-membernone)<br />
[PythonObj.getlink(self)](#pythonobjgetlinkself)<br />
[PytFile()](#pytfile)<br />
[@Property: PytFile.filename](#property-pytfilefilename)<br />
[PytFile.exists(self)](#pytfileexistsself)<br />
[PytFile.read(self)](#pytfilereadself)<br />
[PythonDefinitionObj()](#pythondefinitionobj)<br />
[@Property: PythonDefinitionObj.value](#property-pythondefinitionobjvalue)<br />
[PythonObj()](#pythonobj)<br />
[PythonObj.getlink(self)](#pythonobjgetlinkself)<br />
[TitleObj()](#titleobj)<br />
[@Property: TitleObj.level](#property-titleobjlevel)<br />
[@Property: TitleObj.title](#property-titleobjtitle)<br />
[TitleObj.getanchor(self)](#titleobjgetanchorself)<br />


#### ConvMD()
```python
class ConvMD(object):
```

```
Prepare MD string
```

##### ConvMD.add_tag(begin_tag, end_tag)
```python
def ConvMD.add_tag(begin_tag, end_tag):
```
> <br />
> Decorator - add a tag<br />
> <br />
> <b>Example:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ('__', '__') => __ TXT __<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  beg_tag (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_tag (str)<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />
##### ConvMD.repl_beg_end(begin_regexp, end_regexp, begin_tag, end_tag)
```python
def ConvMD.repl_beg_end(begin_regexp, end_regexp, begin_tag, end_tag):
```
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
##### ConvMD.repl_str(old_string, new_string)
```python
def ConvMD.repl_str(old_string, new_string):
```
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
#### DocString2MD()
```python
class DocString2MD(object):
```

```
Class DocString2MD : export Google docstring to MD File.

Use:
    >>> doc = DocString2MD("docstring2md")
    >>> doc.import_module()
    True
    >>> result = doc.get_doc()
    >>> result = result.split("\n")
    >>> print(result[0])
    # docstring2md
```

##### @Property: DocString2MD.module_name
```python
@property
def DocString2MD.module_name(self):
@module_name.setter
def DocString2MD.module_name(self, module_name):

```
> <br />
> return /path/to/the/json/file<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### DocString2MD.get_doc(self)
```python
def DocString2MD.get_doc(self):
```
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
##### DocString2MD.import_module(self)
```python
def DocString2MD.import_module(self):
```
> <br />
> import all infos<br />
> <br />
#### DocStringObj()
```python
class DocStringObj(object):
```

```
String to store and prepare the docstring.
This object will become an attribut.

Use:
    >>> docstring = DocStringObj("My docstring", PythonObjType.fun)
    >>> print(docstring)
    > <br />
    > My docstring<br />
    > <br />
    >>> docstring = DocStringObj("", PythonObjType.fun)
    >>> print(docstring)
    > <br />
    > <br />
    > <br />
    >>> docstring = DocStringObj("My docstring", PythonObjType.cla)
    >>> print(docstring)
    <BLANKLINE>
    ```
    My docstring
    ```
    <BLANKLINE>
```

##### @Property: DocStringObj.value
```python
@property
def DocStringObj.value(self):
@value.setter
def DocStringObj.value(self, value):

```
> <br />
> Store the docstring<br />
> <br />
#### ExtractPythonModule()
```python
class ExtractPythonModule(object):
```

```
Object in order to extract Python functions, classes....

Use:
    >>> mod = ExtractPythonModule("oups...")
    >>> mod.import_module()
    Traceback (most recent call last):
    ...
    ModuleNotFoundError: No module named 'oups'
    >>> mod = ExtractPythonModule("json")
    >>> mod.import_module()
    True
    >>> mod.extract()
```

##### ExtractPythonModule.extract(self)
```python
def ExtractPythonModule.extract(self):
```
> <br />
> Defines module object and extracts all members.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### ExtractPythonModule.import_module(self)
```python
@__check_module
def ExtractPythonModule.import_module(self):
```
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
#### MembersObj()
```python
class MembersObj(object):
```

```
Dict() to store a python object's members.
This object will become an attribute.
```

##### MembersObj.items(self)
```python
def MembersObj.items(self):
```
> <br />
> get items<br />
> <br />
##### MembersObj.sortkeys(self)
```python
def MembersObj.sortkeys(self):
```
> <br />
> sort the key before using the list<br />
> <br />
#### ModuleObj()
```python
class ModuleObj(PythonObj):
```

```
Class in order to register module informations
__str__ is used to export with MD format.

Use:
    >>> obj = ModuleObj("Mod", "module", "mod doc")
    >>> print(obj)
    mod doc
    ## Dev notes
    <BLANKLINE>
```

##### ModuleObj.getallstr(self, member=None)
```python
def ModuleObj.getallstr(self, member=None):
```
> <br />
> get all definitions and docstring<br />
> <br />
##### ModuleObj.gettoc(self, member=None)
```python
def ModuleObj.gettoc(self, member=None):
```
> <br />
> Get all link and provide a toc<br />
> <br />
##### PythonObj.getlink(self)
```python
def PythonObj.getlink(self):
```
> <br />
> MD Link format<br />
> <br />
#### PytFile()
```python
class PytFile(object):
```

```
>>> data_file = PytFile("lorem")
Traceback (most recent call last):
...
OSError: File not found !
>>> data_file = PytFile(None)
>>> data_file.exists()
False
>>> fstab = PytFile("/etc/fstab")
>>> fstab.filename.stem
'fstab'
>>> fstab
/etc/fstab
>>> # pathlib to run the test everywhere
>>> import pathlib
>>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
>>> license = PytFile(path + "../LICENSE")
>>> license.filename.stem
'LICENSE'
>>> license.exists()
True
>>> #print(license.read())
```

##### @Property: PytFile.filename
```python
@property
def PytFile.filename(self):
@filename.setter
def PytFile.filename(self, value):

```
> <br />
> path to the module<br />
> <br />
##### PytFile.exists(self)
```python
def PytFile.exists(self):
```
> <br />
> file exists<br />
> <br />
##### PytFile.read(self)
```python
def PytFile.read(self):
```
> <br />
> read the text<br />
> <br />
#### PythonDefinitionObj()
```python
class PythonDefinitionObj(object):
```

```
String so store and prepare the object definition:
Example : def function_name(*args)
This object will become an attribute.

Use:
    >>> obj = PythonDefinitionObj(1)
    Traceback (most recent call last):
    ...
    ValueError: PytDefObj: bad value
    >>> obj = PythonDefinitionObj("")
    Traceback (most recent call last):
    ...
    ValueError: PytDefObj: bad value
    >>> obj = PythonDefinitionObj("MyOBJ")
    >>> print(obj)
    ```python
    MyOBJ
    ```
```

##### @Property: PythonDefinitionObj.value
```python
@property
def PythonDefinitionObj.value(self):
@value.setter
def PythonDefinitionObj.value(self, value):

```
> <br />
> Store the value<br />
> <br />
#### PythonObj()
```python
class PythonObj(object):
```

```
Class in order to register object informations
__str__ is used to export with MD format.

Use:
    >>> obj = PythonObj("Mc", "def Mc()", "Doc", 1, PythonObjType.fun)
    >>> print(obj)
    <BLANKLINE>
    #### Mc
    ```python
    def Mc()
    ```
    > <br />
    > Doc<br />
    > <br />
    >>> obj = PythonObj("Mc", "class Mc():", "Doc", 1, PythonObjType.cla)
    >>> print(obj)
    <BLANKLINE>
    #### Mc
    ```python
    class Mc():
    ```
    <BLANKLINE>
    ```
    Doc
    ```
    <BLANKLINE>
```

##### PythonObj.getlink(self)
```python
def PythonObj.getlink(self):
```
> <br />
> MD Link format<br />
> <br />
#### TitleObj()
```python
class TitleObj(object):
```

```
String to store and prepare MD title
This object will become an attribute.

Use:
    >>> title = TitleObj(3, "oups")
    Traceback (most recent call last):
    ...
    ValueError: TitleObj: Title type is string
    >>> title = TitleObj("Test_def(self, var, indx)", 3)
    >>> print(title)
    ###### Test_def(self, var, indx)
    >>> print(title.getanchor())
    test_defself-var-indx
```

##### @Property: TitleObj.level
```python
@property
def TitleObj.level(self):
@level.setter
def TitleObj.level(self, level):

```
> <br />
> Store the level<br />
> <br />
##### @Property: TitleObj.title
```python
@property
def TitleObj.title(self):
@title.setter
def TitleObj.title(self, title):

```
> <br />
> Store the title<br />
> <br />
##### TitleObj.getanchor(self)
```python
def TitleObj.getanchor(self):
```
> <br />
> provide a link to prepare the toc.<br />
> <br />
