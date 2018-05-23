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
[ObjVisitor()](#objvisitor)<br />
[ObjVisitor.get_tree()](#objvisitorget_tree)<br />
[ObjVisitor.visit_Module()](#objvisitorvisit_module)<br />
[ObjVisitor.visit_ClassDef()](#objvisitorvisit_classdef)<br />
[ObjVisitor.visit_FunctionDef()](#objvisitorvisit_functiondef)<br />
[ConvMD()](#convmd)<br />
[ConvMD.repl_str()](#convmdrepl_str)<br />
[ConvMD.repl_str.tags_decorator()](#convmdrepl_strtags_decorator)<br />
[ConvMD.repl_beg_end()](#convmdrepl_beg_end)<br />
[ConvMD.repl_beg_end.tags_decorator()](#convmdrepl_beg_endtags_decorator)<br />
[ConvMD.add_tag()](#convmdadd_tag)<br />
[ConvMD.add_tag.tags_decorator()](#convmdadd_tagtags_decorator)<br />
[DocString2MD()](#docstring2md)<br />
[DocString2MD.import_module()](#docstring2mdimport_module)<br />
[DocString2MD.get_doc()](#docstring2mdget_doc)<br />
[PytFile()](#pytfile)<br />
[@Property PytFile.filename](#property-pytfilefilename)<br />
[PytFile.exists()](#pytfileexists)<br />
[PytFile.read()](#pytfileread)<br />
[PytLog()](#pytlog)<br />
[PytLog.debug()](#pytlogdebug)<br />
[PytLog.warning()](#pytlogwarning)<br />
[PytLog.info()](#pytloginfo)<br />
[PytLog.error()](#pytlogerror)<br />
[PytLog.set_level()](#pytlogset_level)<br />
[PytLog.set_debug()](#pytlogset_debug)<br />
[run()](#run)<br />
[PytMod()](#pytmod)<br />
[@Property PytMod.module](#property-pytmodmodule)<br />
[@Property PytMod.docstring](#property-pytmoddocstring)<br />
[@Property PytMod.pkg_main_docstring](#property-pytmodpkg_main_docstring)<br />
[@Property PytMod.toc](#property-pytmodtoc)<br />
[PytMod.ismodule()](#pytmodismodule)<br />
[PytMod.read()](#pytmodread)<br />

#### ObjVisitor()
```python
class ObjVisitor():
```

```
This Class is an ast.NodeVisitor class and allow us to parse
code tree.
All methods are called according to node type.
We define other private method in order to manage string format.
We use decorator to keep a clean code without MD Tag.

ObjVisitor(module_docstring=True|False)
    module_docstring: true => retrieve the module docstring
    This parameter is usefull to use the first docstring module
    in a package.

Use:
    >>> from docstring2md.file import PytFile
    >>> import pathlib
    >>> module = str(pathlib.Path(__file__).resolve())
    >>> source = PytFile(module)
    >>> # init
    >>> doc = ObjVisitor(module_docstring=False)
    >>> # provide source, generate the tree and use visit mechanisme
    >>> doc.visit(doc.get_tree(source.read()))
    >>> result = doc.output
    >>> result = result.split("\n")
    >>> result[0]
    '#### ObjVisitor()'
    >>> result = doc.toc
    >>> result = result.split("\n")
    >>> result[0]
    '[ObjVisitor()](#objvisitor)<br />'
```

##### ObjVisitor.get_tree()
```python

def ObjVisitor.get_tree(self, source):
```
> <br />
> This function allow us to parse the source and build the<br />
> tree.<br />
> We put this function to group all AST function in this<br />
> module.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  source (str): source code<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  AST tree<br />
> <br />
##### ObjVisitor.visit_Module()
```python

def ObjVisitor.visit_Module(self, node):
```
> <br />
> This function is automatically called by AST mechanisme<br />
> when the current node is a module.<br />
> We update self.output.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  node (ast): current node<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
> <br />
##### ObjVisitor.visit_ClassDef()
```python

def ObjVisitor.visit_ClassDef(self, node):
```
> <br />
> This function is automatically called by AST mechanisme<br />
> when the current node is a class.<br />
> We update self.output.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  node (ast): current node<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
> <br />
##### ObjVisitor.visit_FunctionDef()
```python

def ObjVisitor.visit_FunctionDef(self, node):
```
> <br />
> This function is automatically called by AST mechanisme<br />
> when the current node is a function.<br />
> We update self.output.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  node (ast): current node<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
> <br />
#### ConvMD()
```python
class ConvMD(object):
```

```
Prepare MD string
```

##### ConvMD.repl_str()
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
###### ConvMD.repl_str.tags_decorator()
```python

def ConvMD.repl_str.tags_decorator(func):
```
> <br />
> decorator <br />
> <br />
##### ConvMD.repl_beg_end()
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
###### ConvMD.repl_beg_end.tags_decorator()
```python

def ConvMD.repl_beg_end.tags_decorator(func):
```
> <br />
> decorator <br />
> <br />
##### ConvMD.add_tag()
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
###### ConvMD.add_tag.tags_decorator()
```python

def ConvMD.add_tag.tags_decorator(func):
```
> <br />
> decorator <br />
> <br />
#### DocString2MD()
```python
class DocString2MD(object):
```

```
Class DocString2MD : export Google docstring to MD File.

Use:
    >>> doc = DocString2MD("oups")
    >>> doc.import_module()
    False
    >>> doc = DocString2MD("docstring2md")
    >>> doc.import_module()
    True
    >>> result = doc.get_doc()
    >>> result = result.split("\n")
    >>> print(result[0])
    # docstring2md
```

##### DocString2MD.import_module()
```python

def DocString2MD.import_module(self):
```
> <br />
> import all infos<br />
> <br />
##### DocString2MD.get_doc()
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
>>> result = license.read()
>>> result = result.split("\n")
>>> result[0]
'                    GNU GENERAL PUBLIC LICENSE'
```

##### @Property PytFile.filename
```python
@property
def PytFile.filename(self):
```
> <br />
> path to the module<br />
> <br />
##### PytFile.exists()
```python

def PytFile.exists(self):
```
> <br />
> file exists<br />
> <br />
##### PytFile.read()
```python

def PytFile.read(self):
```
> <br />
> read the text<br />
> <br />
#### PytLog()
```python
class PytLog(object):
```

```
None
```

##### PytLog.debug()
```python

def PytLog.debug(self, msg):
```
> <br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <br />
> <br />
##### PytLog.warning()
```python

def PytLog.warning(self, msg):
```
> <br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <br />
> <br />
##### PytLog.info()
```python

def PytLog.info(self, msg):
```
> <br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <br />
> <br />
##### PytLog.error()
```python

def PytLog.error(self, msg):
```
> <br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <br />
> <br />
##### PytLog.set_level()
```python

def PytLog.set_level(self, sev):
```
> <br />
> None<br />
> <br />
##### PytLog.set_debug()
```python

def PytLog.set_debug(self):
```
> <br />
> None<br />
> <br />
#### run()
```python

def run():
```
> <br />
> This function is called by the CLI runner and manage options.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  print screen|file<br />
> <br />
#### PytMod()
```python
class PytMod(object):
```

```
Object in order to extract Python functions, class....

Use:
    >>> mod = PytMod("oups...")
    >>> mod.read()
    Traceback (most recent call last):
    ...
    ModuleNotFoundError: No module named 'oups'
    >>> mod = PytMod("json")
    >>> mod.read()
    >>> # print(mod.pkg_main_docstring)
    >>> # print(mod.docstring)
```

##### @Property PytMod.module
```python
@property
def PytMod.module(self):
```
> <br />
> <b>module name (str):</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  modulename<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  /path/to/the/mod<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ./path/to/the/mod<br />
> <br />
##### @Property PytMod.docstring
```python
@property
def PytMod.docstring(self):
```
> <br />
> returns all the docstrings.<br />
> <br />
##### @Property PytMod.pkg_main_docstring
```python
@property
def PytMod.pkg_main_docstring(self):
```
> <br />
> PKG only.<br />
> Returns the main docstring.<br />
> <br />
##### @Property PytMod.toc
```python
@property
def PytMod.toc(self):
```
> <br />
> Returns the TOC<br />
> <br />
##### PytMod.ismodule()
```python

def PytMod.ismodule(self):
```
> <br />
> If module name is a module file => True<br />
> Else if the module name is a package => False<br />
> <br />
##### PytMod.read()
```python

def PytMod.read(self):
```
> <br />
> Reads all files and store the result.<br />
> <br />

