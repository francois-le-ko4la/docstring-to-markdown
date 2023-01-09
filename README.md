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
specifications, directly from the source code (Google DocStrings). This can
save a  lot of time  and effort that would otherwise be spent manually
writing documentation. In addition, having documentation automatically
generated from code ensures that it stays up-to-date as the codebase
changes. Overall, this package provides a convenient solution for generating
high-quality documentation for Python projects.

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
Usage: export_docstring2md [-h] [--version] [--debug | --quiet]
                           [--logfile LOGFILE] [--toc] [--private-def] -p
                           PACKAGE [-o OUTPUT_FILE] [-t TOML_FILE]
                           [-mmd MERMAID_FILE]

This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.

Options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
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
    This script exits 0 on success, and >0 if an error occurs.
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
- [X] Add-on : typing
- [ ] Finish the typing
- [ ] AST optimisation
- [ ] Improve CONST
- [ ] Release 0.5.0

## License

This package is distributed under the [GPLv3 license](./LICENSE)
## Dev notes
### TOML file:

```

# -*- coding: utf-8 -*-
[project]
name = "docstring2md"
version = "0.5.0"
authors = [
  {name = "ko4la" }
]
description = "Docstring extractor to generate readme."
requires-python = ">=3.7"
classifiers = [
    "Development Status :: 5 - Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3 :: Only",
]
dependencies = [
    "PyYAML>=3.12",
    "rich>=12.6.0",
    "rich_argparse>=0.6.0",
    "importlib-metadata ~= 1.0 ; python_version < '3.8'"
    ]

[project.optional-dependencies]
dev = [
    "pycodestyle>=2.3.1",
    "pytest>=7.2.0",
    "pylint",
    "mypy",
    "pytest-pylint",
    "pytest-pycodestyle",
    "pytest-mypy",
    "types-setuptools",
    "types-PyYAML"]

[project.scripts]
export_docstring2md = "docstring2md.cli:run"

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
minversion = "7.2"
addopts = "-v -rfEX --pycodestyle --doctest-modules --mypy --pylint --strict-markers"
python_files = ["docstring2md/*.py"]
xfail_strict = true
filterwarnings = [
    "ignore:.*U.*mode is deprecated:DeprecationWarning",
    "ignore::DeprecationWarning"]
[tool.mypy]
mypy_path = "$MYPY_CONFIG_FILE_DIR/stubs"



```

### UML Diagram:

```mermaid

classDiagram
  class DocString2MDOptions {
    export_file
    private_def
    toc
    toml
    uml
  }
  class LoggingMSG {
    debug
    error
    info
  }
  class MyFile {
    exists
    path
    status
    absolute() str
    read() str
    resolve() str
    set_path(path: Union[str, None]) MyFile
    write(data: str) int
  }
  class NodeDef {
    definition
    docstring
    level
    title
    get_definition() str
    get_docstring() str
    get_summary() str
    get_title() str
    get_toc_elem() str
  }
  class NodeVisitor {
    generic_visit(node)
    visit(node)
    visit_Constant(node)
  }
  class PytMod {
    module
    node_lst
    pkg_main_docstring
    ismodule() bool
    read() None
  }
  class Const {
    decorator_tag : str
    dev_head : str
    dev_obj : str
    dev_toml : str
    dev_uml : str
    docstring_empty : str
    function_tag : str
    head_tag : str
    property_tag : str
  }
  class LoggingMSG {
    debug : str
    error : str
    info : str
  }
  class LoggingMSGCollection {
    args
    dump
    elapse_time
    logfile
    python
    result
  }
  class LoggingSetup {
    default_format : str
    default_level : str
    encoding : str
    file_format : str
    logfile : str
    simple_format : str
    set_logfile(path: str) 'LoggingSetup'
  }
  class Tag {
    beg_b : str
    beg_co : str
    beg_mermaid : str
    beg_py : str
    beg_str : str
    cr : str
    end_b : str
    end_bh : str
    end_co : str
    end_py : str
    end_str : str
    end_strh : str
    html_cr : str
    html_tab : str
    quote : str
    tab : str
  }
  class ClassDef {
  }
  class FuncDef {
    get_docstring() str
  }
  class ModuleDef {
  }
  class NodeDef {
    definition : str
    docstring : str
    level : int
    title : str
    get_definition() str
    get_docstring() str
    get_summary() str
    get_title() str
    get_toc_elem() str
  }
  class NodeLink {
    level : int
    parent : Union[ast.FunctionDef, ast.ClassDef, ast.Module]
  }
  class ObjVisitor {
    node_lst
    get_tree(source: str) ast.AST
    visit_ClassDef(node: ast.ClassDef) None
    visit_FunctionDef(node: ast.FunctionDef) None
    visit_Module(node: ast.Module) None
  }
  class ConvMD {
    add_tag(begin_tag: str, end_tag: str) Callable[[F], F]
    repl_beg_end(begin_regexp: str, end_regexp: str, begin_tag: str, end_tag: str) Callable[[F], F]
    repl_str(old_string: str, new_string: str) Callable[[F], F]
  }
  class DocString2MD {
    get_doc() str
    import_module() int
    writedoc() int
  }
  class DocString2MDOptions {
    export_file
    private_def : bool
    toc : bool
    toml
    uml
  }
  class MyFile {
    exists : bool
    path : Union[Path, None]
    status : int
    absolute() str
    read() str
    resolve() str
    set_path(path: Union[str, None]) MyFile
    write(data: str) int
  }
  class PytMod {
    module
    node_lst
    pkg_main_docstring
    ismodule() bool
    read() None
  }
  class NamedTuple {
  }
  Const --|> NamedTuple
  LoggingMSG --|> NamedTuple
  LoggingMSGCollection --|> NamedTuple
  LoggingSetup --|> NamedTuple
  Tag --|> NamedTuple
  ClassDef --|> NodeDef
  FuncDef --|> NodeDef
  ModuleDef --|> NodeDef
  NodeDef --|> NamedTuple
  NodeLink --|> NamedTuple
  ObjVisitor --|> NodeVisitor
  DocString2MDOptions --|> NamedTuple
  MyFile --|> NamedTuple
  DocString2MDOptions --* DocString2MD : __options
  DocString2MDOptions --* DocString2MD : __options
  LoggingMSG --* LoggingMSGCollection : logfile
  LoggingMSG --* LoggingMSGCollection : args
  LoggingMSG --* LoggingMSGCollection : python
  LoggingMSG --* LoggingMSGCollection : dump
  LoggingMSG --* LoggingMSGCollection : result
  LoggingMSG --* LoggingMSGCollection : elapse_time
  MyFile --* DocString2MDOptions : toml
  MyFile --* DocString2MDOptions : uml
  MyFile --* DocString2MDOptions : export_file
  PytMod --* DocString2MD : __my_module
  PytMod --* DocString2MD : __my_module


```

### Objects:

[logger_ast()](#logger_ast)<br />
[logger_ast.func_wrapper()](#logger_astfunc_wrapper)<br />
[NodeLink()](#nodelink)<br />
[NodeDef()](#nodedef)<br />
[NodeDef.get_summary()](#nodedefget_summary)<br />
[NodeDef.get_toc_elem()](#nodedefget_toc_elem)<br />
[NodeDef.get_title()](#nodedefget_title)<br />
[NodeDef.get_definition()](#nodedefget_definition)<br />
[NodeDef.get_docstring()](#nodedefget_docstring)<br />
[ClassDef()](#classdef)<br />
[ClassDef.__new__()](#classdefnew)<br />
[ClassDef.__init__()](#classdefinit)<br />
[FuncDef()](#funcdef)<br />
[FuncDef.__new__()](#funcdefnew)<br />
[FuncDef.__init__()](#funcdefinit)<br />
[FuncDef.get_docstring()](#funcdefget_docstring)<br />
[ModuleDef()](#moduledef)<br />
[ModuleDef.__new__()](#moduledefnew)<br />
[ModuleDef.__init__()](#moduledefinit)<br />
[ObjVisitor()](#objvisitor)<br />
[ObjVisitor.__init__()](#objvisitorinit)<br />
[@Property ObjVisitor.node_lst()](#property-objvisitornode_lst)<br />
[ObjVisitor.get_tree()](#objvisitorget_tree)<br />
[ObjVisitor.__set_level()](#objvisitor__set_level)<br />
[ObjVisitor.__get_fullname()](#objvisitor__get_fullname)<br />
[ObjVisitor.__get_docstring()](#objvisitor__get_docstring)<br />
[ObjVisitor.__get_value_from_name()](#objvisitor__get_value_from_name)<br />
[ObjVisitor.__get_value_from_constant()](#objvisitor__get_value_from_constant)<br />
[ObjVisitor.__get_value_from_num()](#objvisitor__get_value_from_num)<br />
[ObjVisitor.__get_value_from_str()](#objvisitor__get_value_from_str)<br />
[ObjVisitor.__get_value_from_attribute()](#objvisitor__get_value_from_attribute)<br />
[ObjVisitor.__get_value_from_unary()](#objvisitor__get_value_from_unary)<br />
[ObjVisitor.__get_value_from_list()](#objvisitor__get_value_from_list)<br />
[ObjVisitor.__get_value_from_subscript()](#objvisitor__get_value_from_subscript)<br />
[ObjVisitor.__get_value_from_node()](#objvisitor__get_value_from_node)<br />
[ObjVisitor.visit_Module()](#objvisitorvisit_module)<br />
[ObjVisitor.__mod_get_docstring()](#objvisitor__mod_get_docstring)<br />
[ObjVisitor.visit_ClassDef()](#objvisitorvisit_classdef)<br />
[ObjVisitor.__cla_get_title()](#objvisitor__cla_get_title)<br />
[ObjVisitor.__cla_get_def()](#objvisitor__cla_get_def)<br />
[ObjVisitor.__cla_get_inheritance()](#objvisitor__cla_get_inheritance)<br />
[ObjVisitor.__cla_get_docstring()](#objvisitor__cla_get_docstring)<br />
[ObjVisitor.visit_FunctionDef()](#objvisitorvisit_functiondef)<br />
[ObjVisitor.__func_valid_name()](#objvisitor__func_valid_name)<br />
[ObjVisitor.__func_get_title()](#objvisitor__func_get_title)<br />
[ObjVisitor.__func_get_def()](#objvisitor__func_get_def)<br />
[ObjVisitor.__func_get_args()](#objvisitor__func_get_args)<br />
[ObjVisitor.__func_get_args_annotation()](#objvisitor__func_get_args_annotation)<br />
[ObjVisitor.__func_get_args_default()](#objvisitor__func_get_args_default)<br />
[ObjVisitor.__func_get_decorator()](#objvisitor__func_get_decorator)<br />
[ObjVisitor.__func_get_decorator_args()](#objvisitor__func_get_decorator_args)<br />
[ObjVisitor.__func_get_return()](#objvisitor__func_get_return)<br />
[ObjVisitor.__func_get_docstring()](#objvisitor__func_get_docstring)<br />
[check_python()](#check_python)<br />
[get_argparser()](#get_argparser)<br />
[run()](#run)<br />
[ConvMD()](#convmd)<br />
[ConvMD.repl_str()](#convmdrepl_str)<br />
[ConvMD.repl_str.tags_decorator()](#convmdrepl_strtags_decorator)<br />
[ConvMD.repl_str.tags_decorator.func_wrapper()](#convmdrepl_strtags_decoratorfunc_wrapper)<br />
[ConvMD.repl_beg_end()](#convmdrepl_beg_end)<br />
[ConvMD.repl_beg_end.tags_decorator()](#convmdrepl_beg_endtags_decorator)<br />
[ConvMD.repl_beg_end.tags_decorator.func_wrapper()](#convmdrepl_beg_endtags_decoratorfunc_wrapper)<br />
[ConvMD.add_tag()](#convmdadd_tag)<br />
[ConvMD.add_tag.tags_decorator()](#convmdadd_tagtags_decorator)<br />
[ConvMD.add_tag.tags_decorator.func_wrapper()](#convmdadd_tagtags_decoratorfunc_wrapper)<br />
[DocString2MDOptions()](#docstring2mdoptions)<br />
[DocString2MD()](#docstring2md)<br />
[DocString2MD.__init__()](#docstring2mdinit)<br />
[DocString2MD.import_module()](#docstring2mdimport_module)<br />
[DocString2MD.get_doc()](#docstring2mdget_doc)<br />
[DocString2MD.writedoc()](#docstring2mdwritedoc)<br />
[MyFile()](#myfile)<br />
[MyFile.set_path()](#myfileset_path)<br />
[MyFile.__repr__()](#myfilerepr)<br />
[MyFile.read()](#myfileread)<br />
[MyFile.write()](#myfilewrite)<br />
[MyFile.resolve()](#myfileresolve)<br />
[MyFile.absolute()](#myfileabsolute)<br />
[define_logfile()](#define_logfile)<br />
[PytMod()](#pytmod)<br />
[PytMod.__init__()](#pytmodinit)<br />
[@Property PytMod.module()](#property-pytmodmodule)<br />
[@Property PytMod.node_lst()](#property-pytmodnode_lst)<br />
[@Property PytMod.pkg_main_docstring()](#property-pytmodpkg_main_docstring)<br />
[PytMod.ismodule()](#pytmodismodule)<br />
[PytMod.read()](#pytmodread)<br />
[PytMod.__get_doc_from_module()](#pytmod__get_doc_from_module)<br />
[PytMod.__get_module_list()](#pytmod__get_module_list)<br />
[PytMod.__get_doc_from_pkg()](#pytmod__get_doc_from_pkg)<br />
#### logger_ast()
```python
def logger_ast(func: F) -> F:
```
> <br />
> This function is a decorator to use in the AST Navigator Class.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  func: Callable[P, Any]<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Callable[P, Any]<br />
> <br />
##### logger_ast.func_wrapper()
```python
@wraps(func)
def logger_ast.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
> <br />
> None<br />
> <br />
#### NodeLink()
```python
class NodeLink(NamedTuple):
```

```
NamedTuple to link a node with a parent Node
```

#### NodeDef()
```python
class NodeDef(NamedTuple):
```

```
NamedTuple to link a node with a parent Node
```

##### NodeDef.get_summary()
```python
def NodeDef.get_summary(self) -> str:
```
> <br />
> Node summary<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str<br />
> <br />
##### NodeDef.get_toc_elem()
```python
def NodeDef.get_toc_elem(self) -> str:
```
> <br />
> Return a TOC entry for this node<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str<br />
> <br />
##### NodeDef.get_title()
```python
def NodeDef.get_title(self) -> str:
```
> <br />
> Return the node's title<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str<br />
> <br />
##### NodeDef.get_definition()
```python
@ConvMD.add_tag(TAG.beg_py, TAG.end_py)
def NodeDef.get_definition(self) -> str:
```
> <br />
> Return a TOC entry for this node<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str<br />
> <br />
##### NodeDef.get_docstring()
```python
@ConvMD.add_tag(TAG.beg_co, TAG.end_co)
def NodeDef.get_docstring(self) -> str:
```
> <br />
> Return the node's docstring.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str<br />
> <br />
#### ClassDef()
```python
class ClassDef(NodeDef):
```

```
Define a Class node.

Returns:
            ClassDef
```

##### ClassDef.__new__()
```python
def ClassDef.__new__(cls, *args: Any, **kwargs: Any) -> ClassDef:
```
> <br />
> None<br />
> <br />
##### ClassDef.__init__()
```python
def ClassDef.__init__(self, title: str, definition: str, docstring: str, level: int) -> None:
```
> <br />
> None<br />
> <br />
#### FuncDef()
```python
class FuncDef(NodeDef):
```

```
Define a Function node.

Returns:
            FuncDef
```

##### FuncDef.__new__()
```python
def FuncDef.__new__(cls, *args: Any, **kwargs: Any) -> FuncDef:
```
> <br />
> None<br />
> <br />
##### FuncDef.__init__()
```python
def FuncDef.__init__(self, title: str, definition: str, docstring: str, level: int) -> None:
```
> <br />
> None<br />
> <br />
##### FuncDef.get_docstring()
```python
@ConvMD.repl_beg_end(TAG.beg_str, TAG.end_str, TAG.quote, TAG.html_cr)
@ConvMD.repl_beg_end(TAG.beg_str, TAG.end_strh, TAG.beg_b, TAG.end_bh)
@ConvMD.repl_str(TAG.tab, TAG.html_tab)
@ConvMD.add_tag(TAG.cr, TAG.cr)
def FuncDef.get_docstring(self) -> str:
```
> <br />
> None<br />
> <br />
#### ModuleDef()
```python
class ModuleDef(NodeDef):
```

```
Define a Module node.

Returns:
            ModuleDef
```

##### ModuleDef.__new__()
```python
def ModuleDef.__new__(cls, *args: Any, **kwargs: Any) -> ModuleDef:
```
> <br />
> None<br />
> <br />
##### ModuleDef.__init__()
```python
def ModuleDef.__init__(self, title: str, definition: str, docstring: str, level: int) -> None:
```
> <br />
> None<br />
> <br />
#### ObjVisitor()
```python
class ObjVisitor(ast.NodeVisitor):
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

Examples:
            >>> from docstring2md.file import MyFile
            >>> import pathlib
            >>> module = str(pathlib.Path(__file__).resolve())
            >>> source = MyFile.set_path(module)
            >>> # init
            >>> doc = ObjVisitor(module_docstring=False)
            >>> # provide source, generate the tree and use visit mechanism
            >>> doc.visit(doc.get_tree(source.read()))
            >>> result = doc.node_lst
            >>> result[0].title
            'logger_ast()'
            >>> result[0].get_toc_elem()
            '[logger_ast()](#logger_ast)<br />'
            >>> result[0].definition
            'def logger_ast(func: F) -> F:'
```

##### ObjVisitor.__init__()
```python
def ObjVisitor.__init__(self, module_docstring: bool = False, priv: bool = False) -> None:
```
> <br />
> None<br />
> <br />
##### @Property ObjVisitor.node_lst()
```python
@property
def ObjVisitor.node_lst(self) -> deque[Union[ModuleDef, ClassDef, FuncDef, None]]:
```
> <br />
> Return node list<br />
> <br />
##### ObjVisitor.get_tree()
```python
@staticmethod
def ObjVisitor.get_tree(source: str) -> ast.AST:
```
> <br />
> This function allow us to parse the source and build the<br />
> tree.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  source (str): source code<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  AST tree<br />
> <br />
##### ObjVisitor.__set_level()
```python
@logger_ast
def ObjVisitor.__set_level(self, node: Union[ast.Module, ast.ClassDef, ast.FunctionDef], level = 0, parent = None) -> None:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_fullname()
```python
@logger_ast
def ObjVisitor.__get_fullname(self, node: Union[ast.FunctionDef, ast.ClassDef]) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_docstring()
```python
@staticmethod
@logger_ast
def ObjVisitor.__get_docstring(node: Union[ast.Module, ast.ClassDef, ast.FunctionDef]) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_name()
```python
@staticmethod
def ObjVisitor.__get_value_from_name(node: ast.Name) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_constant()
```python
@staticmethod
def ObjVisitor.__get_value_from_constant(node: Union[ast.Constant, ast.NameConstant]) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_num()
```python
@staticmethod
def ObjVisitor.__get_value_from_num(node: ast.Num) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_str()
```python
@staticmethod
def ObjVisitor.__get_value_from_str(node: ast.Str) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_attribute()
```python
@staticmethod
def ObjVisitor.__get_value_from_attribute(node: ast.Attribute) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_unary()
```python
@staticmethod
def ObjVisitor.__get_value_from_unary(node: ast.UnaryOp) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_list()
```python
def ObjVisitor.__get_value_from_list(self, node: ast.List) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_subscript()
```python
def ObjVisitor.__get_value_from_subscript(self, node: ast.Subscript) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__get_value_from_node()
```python
@logger_ast
def ObjVisitor.__get_value_from_node(self, node: Union[ast.Name, ast.Constant, ast.NameConstant, ast.Num, ast.Str, ast.Attribute, ast.Subscript, ast.UnaryOp, ast.List]) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.visit_Module()
```python
@logger_ast
def ObjVisitor.visit_Module(self, node: ast.Module) -> None:
```
> <br />
> This function is automatically called by AST mechanism<br />
> when the current node is a module.<br />
> We update self.node_lst.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  node (ast.AST): current node<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### ObjVisitor.__mod_get_docstring()
```python
def ObjVisitor.__mod_get_docstring(self, node: ast.Module) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.visit_ClassDef()
```python
@logger_ast
def ObjVisitor.visit_ClassDef(self, node: ast.ClassDef) -> None:
```
> <br />
> This function is automatically called by AST mechanism<br />
> when the current node is a class.<br />
> We update self.node_lst.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  node (ast.ClassDef): current node<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### ObjVisitor.__cla_get_title()
```python
@logger_ast
def ObjVisitor.__cla_get_title(self, node: ast.ClassDef) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__cla_get_def()
```python
@logger_ast
def ObjVisitor.__cla_get_def(self, node: ast.ClassDef) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__cla_get_inheritance()
```python
@logger_ast
def ObjVisitor.__cla_get_inheritance(self, node: ast.ClassDef) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__cla_get_docstring()
```python
@logger_ast
def ObjVisitor.__cla_get_docstring(self, node: ast.ClassDef) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.visit_FunctionDef()
```python
@logger_ast
def ObjVisitor.visit_FunctionDef(self, node: ast.FunctionDef) -> None:
```
> <br />
> This function is automatically called by AST mechanism<br />
> when the current node is a function.<br />
> We update self.node_lst.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  node (ast.FunctionDef): current node<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### ObjVisitor.__func_valid_name()
```python
@logger_ast
def ObjVisitor.__func_valid_name(self, node: ast.FunctionDef) -> bool:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_title()
```python
@logger_ast
def ObjVisitor.__func_get_title(self, node: ast.FunctionDef) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_def()
```python
@logger_ast
def ObjVisitor.__func_get_def(self, node: ast.FunctionDef) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_args()
```python
@logger_ast
def ObjVisitor.__func_get_args(self, node: ast.FunctionDef) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_args_annotation()
```python
@logger_ast
def ObjVisitor.__func_get_args_annotation(self, node: ast.arg) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_args_default()
```python
@logger_ast
def ObjVisitor.__func_get_args_default(self, node: ast.FunctionDef) -> list[str]:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_decorator()
```python
@logger_ast
def ObjVisitor.__func_get_decorator(self, node: ast.FunctionDef) -> list[str]:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_decorator_args()
```python
@logger_ast
def ObjVisitor.__func_get_decorator_args(self, node: ast.Call) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_return()
```python
@logger_ast
def ObjVisitor.__func_get_return(self, node: ast.FunctionDef) -> str:
```
> <br />
> None<br />
> <br />
##### ObjVisitor.__func_get_docstring()
```python
@logger_ast
def ObjVisitor.__func_get_docstring(self, node: ast.FunctionDef) -> str:
```
> <br />
> None<br />
> <br />
#### check_python()
```python
def check_python() -> bool:
```
> <br />
> This function check Python version, log the result and return a status<br />
> True/False.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  True if successful, False otherwise.<br />
> <br />
#### get_argparser()
```python
def get_argparser() -> argparse.ArgumentParser:
```
> <br />
> This function describe the argument parser and return it.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ArgumentParser<br />
> <br />
> <b>Examples:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  >>> a = get_argparser()<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  >>> type(a)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <class 'argparse.ArgumentParser'><br />
> <br />
#### run()
```python
def run() -> int:
```
> <br />
> This function is called by the CLI runner and manage options.<br />
> It exits 0 on success, and >0 if an error occurs.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: status<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_OK: 0 -> success<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_CONFIG: 78 -> config error<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_OSFILE: 72 -> Module not found<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_CANTCREAT: 73 -> can't create the file<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_IOERR: 74 -> write error<br />
> <br />
#### ConvMD()
```python
class ConvMD():
```

```
Prepare MD string
```

##### ConvMD.repl_str()
```python
@staticmethod
def ConvMD.repl_str(old_string: str, new_string: str) -> Callable[[F], F]:
```
> <br />
> Decorator - search & replace a string by another string<br />
> Examples: replace space by an HTML tag.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  old_string (str): string to search<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  new_string (str): new string<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />
###### ConvMD.repl_str.tags_decorator()
```python
def ConvMD.repl_str.tags_decorator(func: F) -> F:
```
> <br />
> decorator <br />
> <br />
####### ConvMD.repl_str.tags_decorator.func_wrapper()
```python
@wraps(func)
def ConvMD.repl_str.tags_decorator.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
> <br />
> wrapper <br />
> <br />
##### ConvMD.repl_beg_end()
```python
@staticmethod
def ConvMD.repl_beg_end(begin_regexp: str, end_regexp: str, begin_tag: str, end_tag: str) -> Callable[[F], F]:
```
> <br />
> Decorator - replace the beginning and the end.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  begin_regexp (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_regexp (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  begin_tag (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_tag (str)<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />
> <b>Examples:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  All new lines must be provided with a specific tag<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  > 'Line' <br /><br />
> <br />
###### ConvMD.repl_beg_end.tags_decorator()
```python
def ConvMD.repl_beg_end.tags_decorator(func: F) -> F:
```
> <br />
> decorator <br />
> <br />
####### ConvMD.repl_beg_end.tags_decorator.func_wrapper()
```python
@wraps(func)
def ConvMD.repl_beg_end.tags_decorator.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
> <br />
> wrapper <br />
> <br />
##### ConvMD.add_tag()
```python
@staticmethod
def ConvMD.add_tag(begin_tag: str, end_tag: str) -> Callable[[F], F]:
```
> <br />
> Decorator - add a tag<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  begin_tag (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_tag (str)<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />
> <b>Examples:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ('__', '__') => __ TXT __<br />
> <br />
###### ConvMD.add_tag.tags_decorator()
```python
def ConvMD.add_tag.tags_decorator(func: F) -> F:
```
> <br />
> decorator <br />
> <br />
####### ConvMD.add_tag.tags_decorator.func_wrapper()
```python
@wraps(func)
def ConvMD.add_tag.tags_decorator.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
> <br />
> wrapper <br />
> <br />
#### DocString2MDOptions()
```python
class DocString2MDOptions(NamedTuple):
```

```
This NamedTuple organizes all options with one NamedTuple
    export_file (str): /path/to/doc/file - None by default
    runtime_file (str): /path/to/runtime/file - None by default
    requirements_file (str): /path/to/requiremnt/file - None by default
    uml_file (str): /path/to/uml/file - None by default
    toc (bool): True -> get a table of content
    priv (bool): True -> get private function
```

#### DocString2MD()
```python
class DocString2MD():
```

```
Class DocString2MD : export Google docstring to MD File.

Examples:
            >>> options: DocString2MDOptions = DocString2MDOptions(                            toml=MyFile.set_path(None),                            uml=MyFile.set_path(None),                            export_file=MyFile.set_path(None),                            toc=False,                            private_def=False)
            >>> doc = DocString2MD("oups", options)
            >>> doc.import_module()
            72
            >>> doc = DocString2MD("docstring2md", options)
            >>> doc.import_module()
            0
            >>> result = doc.get_doc()
            >>> result = result.split("\n")
            >>> print(result[0])
            # docstring2md
```

##### DocString2MD.__init__()
```python
def DocString2MD.__init__(self, module_name: str, options: DocString2MDOptions) -> None:
```
> <br />
> Init the class<br />
> This function define default attributs.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  module_name (str): /path/to/module/ or <module_name><br />
> <br />
##### DocString2MD.import_module()
```python
def DocString2MD.import_module(self) -> int:
```
> <br />
> Import the module.<br />
> It exits 0 on success, and >0 if an error occurs.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: status<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_OK: 0 -> success<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_OSFILE: 72 -> Module not found<br />
> <br />
##### DocString2MD.get_doc()
```python
def DocString2MD.get_doc(self) -> str:
```
> <br />
> Returns the documentation<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str: doc<br />
> <br />
##### DocString2MD.writedoc()
```python
def DocString2MD.writedoc(self) -> int:
```
> <br />
> Writes the doc: screen or files.<br />
> It exits 0 on success, and >0 if an error occurs.<br />
> <br />
> <b>args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: status<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_OK: 0 -> success<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_CANTCREAT: 73 -> can't create the file<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_IOERR: 74 -> write error<br />
> <br />
#### MyFile()
```python
class MyFile(NamedTuple):
```

```
This class describe a file with a NamedTuple
@classmethod is used to init the objects correctly.

Notes:
            The objective is to define a file with only one NamedTuple.
            The NamedTuple will be created by the set_path function to
            define the path.

Examples:
            >>> data_file = MyFile.set_path("lorem")
            >>> data_file.status
            72
            >>> fstab = MyFile.set_path("/etc/fstab")
            >>> fstab.path.stem
            'fstab'
            >>> fstab
            MyFile(path=PosixPath('/etc/fstab'), exists=False, status=72)
            >>> fstab.absolute()
            '/etc/fstab'
            >>> # pathlib to run the test everywhere
            >>> import pathlib
            >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
            >>> lic = MyFile.set_path(f"{path}../../LICENSE")
            >>> lic.path.stem
            'LICENSE'
            >>> lic.exists
            True
            >>> result = lic.read()
            >>> result = result.split("\n")
            >>> result[0]
            '                    GNU GENERAL PUBLIC LICENSE'
```

##### MyFile.set_path()
```python
@classmethod
def MyFile.set_path(cls, path: Union[str, None]) -> MyFile:
```
> <br />
> This function create the MyFile object with the file's path.<br />
> if path = None then return None<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  path: The file's path.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  MyFile or None<br />
> <br />
##### MyFile.__repr__()
```python
def MyFile.__repr__(self) -> str:
```
> <br />
> None<br />
> <br />
##### MyFile.read()
```python
def MyFile.read(self) -> str:
```
> <br />
> read the text<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str: Text if successful else ""<br />
> <br />
##### MyFile.write()
```python
def MyFile.write(self, data: str) -> int:
```
> <br />
> Write data in the file<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int: status<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_OK: 0 -> success<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_CANTCREAT: 73 -> can't create the file<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - EX_IOERR: 74 -> write error<br />
> <br />
##### MyFile.resolve()
```python
def MyFile.resolve(self) -> str:
```
> <br />
> get path.resolve()<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str<br />
> <br />
##### MyFile.absolute()
```python
def MyFile.absolute(self) -> str:
```
> <br />
> get path.absolute()<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str<br />
> <br />
#### define_logfile()
```python
def define_logfile(path: str) -> None:
```
> <br />
> This function set up the log to push log events in the report file.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  path:str&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  /path/to/logfile<br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
#### PytMod()
```python
class PytMod():
```

```
Object in order to extract Python functions, class....

Examples:
            >>> mod = PytMod("oups...")
            >>> mod.read()
            Traceback (most recent call last):
            ...
            ModuleNotFoundError: No module named 'oups'
            >>> mod = PytMod("json")
            >>> mod.read()
            >>> print(mod.node_lst[0].definition)
            class JSONDecodeError(ValueError):
            >>> mod = PytMod(__file__)
            >>> mod.read()
            >>> print(mod.node_lst[0].docstring)
            This script is free software; you can redistribute it and/or
            modify it under the terms of the GNU Lesser General Public
            License as published by the Free Software Foundation; either
            ...
            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
            >>> mod = PytMod('docstring2md')
            >>> mod.read()
            >>> print(mod.node_lst[0].definition)
            def logger_ast(func: F) -> F:
```

##### PytMod.__init__()
```python
def PytMod.__init__(self, module_name: str, priv: bool = False) -> None:
```
> <br />
> None<br />
> <br />
##### @Property PytMod.module()
```python
@property
def PytMod.module(self) -> str:
```
> <br />
> <b>module name (str):</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  modulename<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  /path/to/the/mod<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ./path/to/the/mod<br />
> <br />
##### @Property PytMod.node_lst()
```python
@property
def PytMod.node_lst(self) -> deque[Union[ModuleDef, ClassDef, FuncDef, None]]:
```
> <br />
> returns all the docstrings.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str: Docstring<br />
> <br />
##### @Property PytMod.pkg_main_docstring()
```python
@property
def PytMod.pkg_main_docstring(self) -> deque[Union[ModuleDef, ClassDef, FuncDef, None]]:
```
> <br />
> PKG only.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str: Main docstring<br />
> <br />
##### PytMod.ismodule()
```python
def PytMod.ismodule(self) -> bool:
```
> <br />
> If module name is a module file => True<br />
> Else if the module name is a package => False<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: It exits True on success, and False otherwise.<br />
> <br />
##### PytMod.read()
```python
def PytMod.read(self) -> None:
```
> <br />
> Reads all files and store the result.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
##### PytMod.__get_doc_from_module()
```python
def PytMod.__get_doc_from_module(self, module: str, module_docstring: bool = False) -> deque[Union[ModuleDef, ClassDef, FuncDef, None]]:
```
> <br />
> None<br />
> <br />
##### PytMod.__get_module_list()
```python
def PytMod.__get_module_list(self, package: str) -> list[str]:
```
> <br />
> None<br />
> <br />
##### PytMod.__get_doc_from_pkg()
```python
def PytMod.__get_doc_from_pkg(self, package: str) -> deque[Union[ModuleDef, ClassDef, FuncDef, None]]:
```
> <br />
> None<br />
> <br />