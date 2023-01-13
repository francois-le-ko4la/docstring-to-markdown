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
## Dev notes
### TOML file:

```toml

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
    warning
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
    coma : str
    decorator_tag : str
    dev_head : str
    dev_obj : str
    dev_toml : str
    dev_uml : str
    docstring_empty : str
    dot : str
    function_tag : str
    head_tag : str
    property_tag : str
  }
  class LoggingMSG {
    debug : str
    error : str
    info : str
    warning : str
  }
  class LoggingMSGCollection {
    args
    dump
    elapse_time
    file_not_found
    io_err
    logfile
    new_class
    new_func
    new_module
    node_link_analysis_beg
    node_link_analysis_end
    python
    pytmod
    pytmod_extract
    pytmod_mod
    pytmod_script
    result
    unknown_type_of_node
    write_doc
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
    beg_pre : str
    beg_py : str
    beg_str : str
    beg_toml : str
    coma : str
    cr : str
    end_b : str
    end_bh : str
    end_co : str
    end_pre : str
    end_py : str
    end_str : str
    end_strh : str
    html_cr : str
    html_tab : str
    quote : str
    tab : str
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
    colorize_examples() Callable[[F], F]
    html_escape() Callable[[F], F]
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
  LoggingMSG --* LoggingMSGCollection : pytmod
  LoggingMSG --* LoggingMSGCollection : pytmod_mod
  LoggingMSG --* LoggingMSGCollection : pytmod_script
  LoggingMSG --* LoggingMSGCollection : pytmod_extract
  LoggingMSG --* LoggingMSGCollection : new_module
  LoggingMSG --* LoggingMSGCollection : new_class
  LoggingMSG --* LoggingMSGCollection : new_func
  LoggingMSG --* LoggingMSGCollection : node_link_analysis_beg
  LoggingMSG --* LoggingMSGCollection : node_link_analysis_end
  LoggingMSG --* LoggingMSGCollection : unknown_type_of_node
  LoggingMSG --* LoggingMSGCollection : io_err
  LoggingMSG --* LoggingMSGCollection : file_not_found
  LoggingMSG --* LoggingMSGCollection : write_doc
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
[ConvMD.html_escape()](#convmdhtml_escape)<br />
[ConvMD.html_escape.tags_decorator()](#convmdhtml_escapetags_decorator)<br />
[ConvMD.html_escape.tags_decorator.func_wrapper()](#convmdhtml_escapetags_decoratorfunc_wrapper)<br />
[ConvMD.colorize_examples()](#convmdcolorize_examples)<br />
[ConvMD.colorize_examples.tags_decorator()](#convmdcolorize_examplestags_decorator)<br />
[ConvMD.colorize_examples.tags_decorator.func_wrapper()](#convmdcolorize_examplestags_decoratorfunc_wrapper)<br />
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
<pre>

This function is a decorator to use in the AST Navigator Class.

<b>Args:</b>
            func: F (Callable[..., Any])

<b>Returns:</b>
            F (Callable[..., Any])

</pre>
##### logger_ast.func_wrapper()
```python
@wrapsfunc
def logger_ast.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
<pre>

None

</pre>
#### NodeLink()
```python
class NodeLink(NamedTuple):
```
<pre>

NamedTuple to link a node with a parent Node

</pre>
#### NodeDef()
```python
class NodeDef(NamedTuple):
```
<pre>

NamedTuple to define a node

</pre>
##### NodeDef.get_summary()
```python
def NodeDef.get_summary(self) -> str:
```
<pre>

Node summary

<b>Returns:</b>
            str

</pre>
##### NodeDef.get_toc_elem()
```python
def NodeDef.get_toc_elem(self) -> str:
```
<pre>

Return a TOC entry for this node

<b>Returns:</b>
            str

</pre>
##### NodeDef.get_title()
```python
def NodeDef.get_title(self) -> str:
```
<pre>

Return the node&#x27;s title

<b>Returns:</b>
            str

</pre>
##### NodeDef.get_definition()
```python
@ConvMD.add_tagTAG.beg_py, TAG.end_py
def NodeDef.get_definition(self) -> str:
```
<pre>

Return a TOC entry for this node

<b>Returns:</b>
            str

</pre>
##### NodeDef.get_docstring()
```python
@ConvMD.repl_beg_endTAG.beg_str, TAG.end_strh, TAG.beg_b, TAG.end_bh
@ConvMD.colorize_examples
@ConvMD.html_escape
@ConvMD.add_tagTAG.cr, TAG.cr
def NodeDef.get_docstring(self) -> str:
```
<pre>

Generate the Function&#x27;s Docstring with MD Tag.

<b>Returns:</b>
            str: Docstring

</pre>
#### ObjVisitor()
```python
class ObjVisitor(ast.NodeVisitor):
```
<pre>

This Class is an ast.NodeVisitor class and allow us to parse
code tree.
All methods are called according to node type.
We define other private method in order to manage string format.
We use decorator to keep a clean code without MD Tag.

ObjVisitor(module_docstring=True|False)
    module_docstring: true =&gt; retrieve the module docstring
    This parameter is usefull to use the first docstring module
    in a package.

</pre>
<b>Examples:</b>
```python

            &gt;&gt;&gt; from docstring2md.file import MyFile
            &gt;&gt;&gt; import pathlib
            &gt;&gt;&gt; module = str(pathlib.Path(__file__).resolve())
            &gt;&gt;&gt; source = MyFile.set_path(module)
            &gt;&gt;&gt; # init
            &gt;&gt;&gt; doc = ObjVisitor(module_docstring=False)
            &gt;&gt;&gt; # provide source, generate the tree and use visit mechanism
            &gt;&gt;&gt; doc.visit(doc.get_tree(source.read()))
            &gt;&gt;&gt; result = doc.node_lst
            &gt;&gt;&gt; result[0].title
            &#x27;logger_ast()&#x27;
            &gt;&gt;&gt; result[0].get_toc_elem()
            &#x27;[logger_ast()](#logger_ast)&lt;br /&gt;&#x27;
            &gt;&gt;&gt; result[0].definition
            &#x27;def logger_ast(func: F) -&gt; F:&#x27;


```

##### ObjVisitor.__init__()
```python
def ObjVisitor.__init__(self, module_docstring: bool = False, priv: bool = False) -> None:
```
<pre>

None

</pre>
##### @Property ObjVisitor.node_lst()
```python
@property
def ObjVisitor.node_lst(self) -> deque[Union[NodeDef, None]]:
```
<pre>

Return node list

</pre>
##### ObjVisitor.get_tree()
```python
@staticmethod
def ObjVisitor.get_tree(source: str) -> ast.AST:
```
<pre>

This function allow us to parse the source and build the
tree.

<b>Args:</b>
            source (str): source code

<b>Returns:</b>
            AST tree

</pre>
##### ObjVisitor.__set_level()
```python
@logger_ast
def ObjVisitor.__set_level(self, node: Union[ast.Module, ast.ClassDef, ast.FunctionDef], level = 0, parent = None) -> None:
```
<pre>

None

</pre>
##### ObjVisitor.__get_fullname()
```python
@logger_ast
def ObjVisitor.__get_fullname(self, node: Union[ast.FunctionDef, ast.ClassDef]) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_docstring()
```python
@staticmethod
@logger_ast
def ObjVisitor.__get_docstring(node: Union[ast.Module, ast.ClassDef, ast.FunctionDef]) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_name()
```python
@staticmethod
def ObjVisitor.__get_value_from_name(node: ast.Name) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_constant()
```python
@staticmethod
def ObjVisitor.__get_value_from_constant(node: Union[ast.Constant, ast.NameConstant]) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_num()
```python
@staticmethod
def ObjVisitor.__get_value_from_num(node: ast.Num) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_str()
```python
@staticmethod
def ObjVisitor.__get_value_from_str(node: ast.Str) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_attribute()
```python
@staticmethod
def ObjVisitor.__get_value_from_attribute(node: ast.Attribute) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_unary()
```python
@staticmethod
def ObjVisitor.__get_value_from_unary(node: ast.UnaryOp) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_list()
```python
def ObjVisitor.__get_value_from_list(self, node: ast.List) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_subscript()
```python
def ObjVisitor.__get_value_from_subscript(self, node: ast.Subscript) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__get_value_from_node()
```python
@logger_ast
def ObjVisitor.__get_value_from_node(self, node: Union[ast.Name, ast.Constant, ast.NameConstant, ast.Num, ast.Str, ast.Attribute, ast.Subscript, ast.UnaryOp, ast.List]) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.visit_Module()
```python
@logger_ast
def ObjVisitor.visit_Module(self, node: ast.Module) -> None:
```
<pre>

This function is automatically called by AST mechanism
when the current node is a module.
We update self.node_lst.

<b>Args:</b>
            node (ast.AST): current node

<b>Returns:</b>
            None

</pre>
##### ObjVisitor.__mod_get_docstring()
```python
def ObjVisitor.__mod_get_docstring(self, node: ast.Module) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.visit_ClassDef()
```python
@logger_ast
def ObjVisitor.visit_ClassDef(self, node: ast.ClassDef) -> None:
```
<pre>

This function is automatically called by AST mechanism
when the current node is a class.
We update self.node_lst.

<b>Args:</b>
            node (ast.ClassDef): current node

<b>Returns:</b>
            None

</pre>
##### ObjVisitor.__cla_get_title()
```python
@logger_ast
def ObjVisitor.__cla_get_title(self, node: ast.ClassDef) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__cla_get_def()
```python
@logger_ast
def ObjVisitor.__cla_get_def(self, node: ast.ClassDef) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__cla_get_inheritance()
```python
@logger_ast
def ObjVisitor.__cla_get_inheritance(self, node: ast.ClassDef) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__cla_get_docstring()
```python
@logger_ast
def ObjVisitor.__cla_get_docstring(self, node: ast.ClassDef) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.visit_FunctionDef()
```python
@logger_ast
def ObjVisitor.visit_FunctionDef(self, node: ast.FunctionDef) -> None:
```
<pre>

This function is automatically called by AST mechanism
when the current node is a function.
We add FuncDef obj in self.node_lst.

<b>Args:</b>
            node (ast.FunctionDef): current node

<b>Returns:</b>
            None

</pre>
##### ObjVisitor.__func_valid_name()
```python
@logger_ast
def ObjVisitor.__func_valid_name(self, node: ast.FunctionDef) -> bool:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_title()
```python
@logger_ast
def ObjVisitor.__func_get_title(self, node: ast.FunctionDef) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_def()
```python
@logger_ast
def ObjVisitor.__func_get_def(self, node: ast.FunctionDef) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_args()
```python
@logger_ast
def ObjVisitor.__func_get_args(self, node: ast.FunctionDef) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_args_annotation()
```python
@logger_ast
def ObjVisitor.__func_get_args_annotation(self, node: ast.arg) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_args_default()
```python
@logger_ast
def ObjVisitor.__func_get_args_default(self, node: ast.FunctionDef) -> list[str]:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_decorator()
```python
@logger_ast
def ObjVisitor.__func_get_decorator(self, node: ast.FunctionDef) -> list[str]:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_decorator_args()
```python
@logger_ast
def ObjVisitor.__func_get_decorator_args(self, node: ast.Call) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_return()
```python
@logger_ast
def ObjVisitor.__func_get_return(self, node: ast.FunctionDef) -> str:
```
<pre>

None

</pre>
##### ObjVisitor.__func_get_docstring()
```python
@logger_ast
def ObjVisitor.__func_get_docstring(self, node: ast.FunctionDef) -> str:
```
<pre>

None

</pre>
#### check_python()
```python
def check_python() -> bool:
```
<pre>

This function check Python version, log the result and return a status
True/False.

<b>Returns:</b>
            True if successful, False otherwise.

</pre>
#### get_argparser()
```python
def get_argparser() -> argparse.ArgumentParser:
```
<pre>

This function describe the argument parser and return it.

<b>Returns:</b>
            ArgumentParser

</pre>
<b>Examples:</b>
```python

            &gt;&gt;&gt; a = get_argparser()
            &gt;&gt;&gt; type(a)
            &lt;class &#x27;argparse.ArgumentParser&#x27;&gt;


```

#### run()
```python
def run() -> int:
```
<pre>

This function is called by the CLI runner and manage options.
It exits 0 on success, and &gt;0 if an error occurs.

<b>Returns:</b>
            int: status
            return EX_OK: 0 -&gt; success
            return EX_CONFIG: 78 -&gt; config error
            return EX_OSFILE: 72 -&gt; Module not found
            return EX_CANTCREAT: 73 -&gt; can&#x27;t create the file
            return EX_IOERR: 74 -&gt; write error

</pre>
#### ConvMD()
```python
class ConvMD():
```
<pre>

Prepare MD string

</pre>
##### ConvMD.repl_str()
```python
@staticmethod
def ConvMD.repl_str(old_string: str, new_string: str) -> Callable[[F], F]:
```
<pre>

Decorator - search &amp; replace a string by another string
Examples: replace space by an HTML tag.

<b>Args:</b>
            old_string (str): string to search
            new_string (str): new string

<b>Returns:</b>
            Callable[[F], F]

</pre>
<b>Examples:</b>
```python


            &gt;&gt;&gt; from docstring2md.convmd import ConvMD
            &gt;&gt;&gt; @ConvMD.repl_str(&quot;docstring&quot;, &quot;is ok !&quot;)
            ... def return_test() -&gt; str:
            ...     return &quot;my function docstring&quot;
            &gt;&gt;&gt; print(return_test())
            my function is ok !


```

###### ConvMD.repl_str.tags_decorator()
```python
def ConvMD.repl_str.tags_decorator(func: F) -> F:
```
<pre>

decorator 

</pre>
####### ConvMD.repl_str.tags_decorator.func_wrapper()
```python
@wrapsfunc
def ConvMD.repl_str.tags_decorator.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
<pre>

wrapper 

</pre>
##### ConvMD.repl_beg_end()
```python
@staticmethod
def ConvMD.repl_beg_end(begin_regexp: str, end_regexp: str, begin_tag: str, end_tag: str) -> Callable[[F], F]:
```
<pre>

Decorator - replace the beginning and the end.

<b>Args:</b>
            begin_regexp (str)
            end_regexp (str)
            begin_tag (str)
            end_tag (str)

<b>Returns:</b>
            decorated function

</pre>
<b>Examples:</b>
```python


            &gt;&gt;&gt; # All new lines must be provided with a specific tag
            &gt;&gt;&gt; # &gt; &#x27;Line&#x27; &lt;br /&gt;
            &gt;&gt;&gt; from docstring2md.convmd import ConvMD
            &gt;&gt;&gt; @ConvMD.repl_beg_end(&quot;^&quot;, &quot;$&quot;, &quot;&gt;&quot;, &quot;&lt;br /&gt;&quot;)
            ... def return_test() -&gt; str:
            ...     return &quot;my function docstring&quot;
            &gt;&gt;&gt; print(return_test())
            &gt;my function docstring&lt;br /&gt;


```

###### ConvMD.repl_beg_end.tags_decorator()
```python
def ConvMD.repl_beg_end.tags_decorator(func: F) -> F:
```
<pre>

decorator 

</pre>
####### ConvMD.repl_beg_end.tags_decorator.func_wrapper()
```python
@wrapsfunc
def ConvMD.repl_beg_end.tags_decorator.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
<pre>

wrapper 

</pre>
##### ConvMD.add_tag()
```python
@staticmethod
def ConvMD.add_tag(begin_tag: str, end_tag: str) -> Callable[[F], F]:
```
<pre>

Decorator - add a tag

<b>Args:</b>
            begin_tag (str)
            end_tag (str)

<b>Returns:</b>
            decorated function

</pre>
<b>Examples:</b>
```python

            &gt;&gt;&gt; # (&#x27;__&#x27;, &#x27;__&#x27;) =&gt; __ TXT __
            &gt;&gt;&gt; from docstring2md.convmd import ConvMD
            &gt;&gt;&gt; @ConvMD.add_tag(&quot;__&quot;, &quot;__&quot;)
            ... def return_test() -&gt; str:
            ...     return &quot;test&quot;
            &gt;&gt;&gt; print(return_test())
            __test__


```

###### ConvMD.add_tag.tags_decorator()
```python
def ConvMD.add_tag.tags_decorator(func: F) -> F:
```
<pre>

decorator 

</pre>
####### ConvMD.add_tag.tags_decorator.func_wrapper()
```python
@wrapsfunc
def ConvMD.add_tag.tags_decorator.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
<pre>

wrapper 

</pre>
##### ConvMD.html_escape()
```python
@staticmethod
def ConvMD.html_escape() -> Callable[[F], F]:
```
<pre>

Escape the HTML tag.

<b>Returns:</b>
            decorated function

</pre>
###### ConvMD.html_escape.tags_decorator()
```python
def ConvMD.html_escape.tags_decorator(func: F) -> F:
```
<pre>

decorator 

</pre>
####### ConvMD.html_escape.tags_decorator.func_wrapper()
```python
@wrapsfunc
def ConvMD.html_escape.tags_decorator.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
<pre>

wrapper 

</pre>
##### ConvMD.colorize_examples()
```python
@staticmethod
def ConvMD.colorize_examples() -> Callable[[F], F]:
```
<pre>

Colorize python example.

<b>Returns:</b>
            decorated function

</pre>
###### ConvMD.colorize_examples.tags_decorator()
```python
def ConvMD.colorize_examples.tags_decorator(func: F) -> F:
```
<pre>

decorator 

</pre>
####### ConvMD.colorize_examples.tags_decorator.func_wrapper()
```python
@wrapsfunc
def ConvMD.colorize_examples.tags_decorator.func_wrapper(*args: Any, **kwargs: Any) -> Any:
```
<pre>

wrapper 

</pre>
#### DocString2MDOptions()
```python
class DocString2MDOptions(NamedTuple):
```
<pre>

This NamedTuple organizes all options with one NamedTuple
    export_file (str): /path/to/doc/file - None by default
    runtime_file (str): /path/to/runtime/file - None by default
    requirements_file (str): /path/to/requiremnt/file - None by default
    uml_file (str): /path/to/uml/file - None by default
    toc (bool): True -&gt; get a table of content
    priv (bool): True -&gt; get private function

</pre>
#### DocString2MD()
```python
class DocString2MD():
```
<pre>

Class DocString2MD : export Google docstring to MD File.

</pre>
<b>Examples:</b>
```python

            &gt;&gt;&gt; options: DocString2MDOptions = DocString2MDOptions(
            ...         toml=MyFile.set_path(None),
            ...         uml=MyFile.set_path(None),
            ...         export_file=MyFile.set_path(None),
            ...         toc=False,
            ...         private_def=False)
            &gt;&gt;&gt; doc = DocString2MD(&quot;oups&quot;, options)
            &gt;&gt;&gt; doc.import_module()
            72
            &gt;&gt;&gt; doc = DocString2MD(&quot;docstring2md&quot;, options)
            &gt;&gt;&gt; doc.import_module()
            0
            &gt;&gt;&gt; result = doc.get_doc()
            &gt;&gt;&gt; result = result.split(&quot;\n&quot;)
            &gt;&gt;&gt; print(result[0])
            # docstring2md


```

##### DocString2MD.__init__()
```python
def DocString2MD.__init__(self, module_name: str, options: DocString2MDOptions) -> None:
```
<pre>

Init the class
This function define default attributs.

<b>Args:</b>
            module_name (str): /path/to/module/ or &lt;module_name&gt;

</pre>
##### DocString2MD.import_module()
```python
def DocString2MD.import_module(self) -> int:
```
<pre>

Import the module.
It exits 0 on success, and &gt;0 if an error occurs.

<b>Returns:</b>
            int: status
            return EX_OK: 0 -&gt; success
            return EX_OSFILE: 72 -&gt; Module not found

</pre>
##### DocString2MD.get_doc()
```python
def DocString2MD.get_doc(self) -> str:
```
<pre>

Returns the documentation

<b>Returns:</b>
            str: doc

</pre>
##### DocString2MD.writedoc()
```python
def DocString2MD.writedoc(self) -> int:
```
<pre>

Writes the doc: screen or files.
It exits 0 on success, and &gt;0 if an error occurs.

<b>args:</b>
            None

<b>Returns:</b>
            int: status
            return EX_OK: 0 -&gt; success
            return EX_CANTCREAT: 73 -&gt; can&#x27;t create the file
            return EX_IOERR: 74 -&gt; write error

</pre>
#### MyFile()
```python
class MyFile(NamedTuple):
```
<pre>

This class describe a file with a NamedTuple
@classmethod is used to init the objects correctly.

<b>Notes:</b>
            The objective is to define a file with only one NamedTuple.
            The NamedTuple will be created by the set_path function to
            define the path.

</pre>
<b>Examples:</b>
```python

            &gt;&gt;&gt; data_file = MyFile.set_path(&quot;lorem&quot;)
            &gt;&gt;&gt; data_file.status
            72
            &gt;&gt;&gt; fstab = MyFile.set_path(&quot;/etc/fstab&quot;)
            &gt;&gt;&gt; fstab.path.stem
            &#x27;fstab&#x27;
            &gt;&gt;&gt; fstab
            MyFile(path=PosixPath(&#x27;/etc/fstab&#x27;), exists=False, status=72)
            &gt;&gt;&gt; fstab.absolute()
            &#x27;/etc/fstab&#x27;
            &gt;&gt;&gt; # pathlib to run the test everywhere
            &gt;&gt;&gt; import pathlib
            &gt;&gt;&gt; path = str(pathlib.Path(__file__).resolve().parent) + &quot;/&quot;
            &gt;&gt;&gt; lic = MyFile.set_path(f&quot;{path}../../LICENSE&quot;)
            &gt;&gt;&gt; lic.path.stem
            &#x27;LICENSE&#x27;
            &gt;&gt;&gt; lic.exists
            True
            &gt;&gt;&gt; result = lic.read()
            &gt;&gt;&gt; result = result.split(&quot;\n&quot;)
            &gt;&gt;&gt; result[0]
            &#x27;                    GNU GENERAL PUBLIC LICENSE&#x27;


```

##### MyFile.set_path()
```python
@classmethod
def MyFile.set_path(cls, path: Union[str, None]) -> MyFile:
```
<pre>

This function create the MyFile object with the file&#x27;s path.
if path = None then return None

<b>Args:</b>
            path: The file&#x27;s path.

<b>Returns:</b>
            MyFile or None

</pre>
##### MyFile.__repr__()
```python
def MyFile.__repr__(self) -> str:
```
<pre>

None

</pre>
##### MyFile.read()
```python
def MyFile.read(self) -> str:
```
<pre>

read the text

<b>Returns:</b>
            str: Text if successful else &quot;&quot;

</pre>
##### MyFile.write()
```python
def MyFile.write(self, data: str) -> int:
```
<pre>

Write data in the file

<b>Returns:</b>
            int: status
            return EX_OK: 0 -&gt; success
            return EX_CANTCREAT: 73 -&gt; can&#x27;t create the file
            return EX_IOERR: 74 -&gt; write error

</pre>
##### MyFile.resolve()
```python
def MyFile.resolve(self) -> str:
```
<pre>

get path.resolve()

<b>Returns:</b>
            str

</pre>
##### MyFile.absolute()
```python
def MyFile.absolute(self) -> str:
```
<pre>

get path.absolute()

<b>Returns:</b>
            str

</pre>
#### define_logfile()
```python
def define_logfile(path: str) -> None:
```
<pre>

This function set up the log to push log events in the report file.

<b>Args:</b>
            path:str    /path/to/logfile
<b>Returns:</b>
            None

</pre>
#### PytMod()
```python
class PytMod():
```
<pre>

Object in order to extract Python functions, class....

</pre>
<b>Examples:</b>
```python

            &gt;&gt;&gt; mod = PytMod(&quot;oups...&quot;)
            &gt;&gt;&gt; mod.read()
            Traceback (most recent call last):
            ...
            ModuleNotFoundError: No module named &#x27;oups&#x27;
            &gt;&gt;&gt; mod = PytMod(&quot;json&quot;)
            &gt;&gt;&gt; mod.read()
            &gt;&gt;&gt; print(mod.node_lst[0].definition)
            class JSONDecodeError(ValueError):
            &gt;&gt;&gt; mod = PytMod(__file__)
            &gt;&gt;&gt; mod.read()
            &gt;&gt;&gt; print(mod.node_lst[0].docstring)
            This script is free software; you can redistribute it and/or
            modify it under the terms of the GNU Lesser General Public
            License as published by the Free Software Foundation; either
            ...
            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
            &gt;&gt;&gt; mod = PytMod(&#x27;docstring2md&#x27;)
            &gt;&gt;&gt; mod.read()
            &gt;&gt;&gt; print(mod.node_lst[0].definition)
            def logger_ast(func: F) -&gt; F:


```

##### PytMod.__init__()
```python
def PytMod.__init__(self, module_name: str, priv: bool = False) -> None:
```
<pre>

None

</pre>
##### @Property PytMod.module()
```python
@property
def PytMod.module(self) -> str:
```
<pre>

module name (str):
    modulename
    /path/to/the/mod
    ./path/to/the/mod

</pre>
##### @Property PytMod.node_lst()
```python
@property
def PytMod.node_lst(self) -> deque[Union[NodeDef, None]]:
```
<pre>

returns all the docstrings.

<b>Returns:</b>
            str: Docstring

</pre>
##### @Property PytMod.pkg_main_docstring()
```python
@property
def PytMod.pkg_main_docstring(self) -> deque[Union[NodeDef, None]]:
```
<pre>

PKG only.

<b>Returns:</b>
            str: Main docstring

</pre>
##### PytMod.ismodule()
```python
def PytMod.ismodule(self) -> bool:
```
<pre>

If module name is a module file =&gt; True
Else if the module name is a package =&gt; False

<b>Returns:</b>
            bool: It exits True on success, and False otherwise.

</pre>
##### PytMod.read()
```python
def PytMod.read(self) -> None:
```
<pre>

Reads all files and store the result.

<b>Returns:</b>
            None

</pre>
##### PytMod.__get_doc_from_module()
```python
def PytMod.__get_doc_from_module(self, module: str, module_docstring: bool = False) -> deque[Union[NodeDef, None]]:
```
<pre>

None

</pre>
##### PytMod.__get_module_list()
```python
def PytMod.__get_module_list(self, package: str) -> list[str]:
```
<pre>

None

</pre>
##### PytMod.__get_doc_from_pkg()
```python
def PytMod.__get_doc_from_pkg(self, package: str) -> deque[Union[NodeDef, None]]:
```
<pre>

None

</pre>