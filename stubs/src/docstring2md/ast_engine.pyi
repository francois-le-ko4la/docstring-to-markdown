import ast
from collections import deque
from typing import Any, Callable, NamedTuple, TypeVar, Union

F = TypeVar('F', bound=Callable[..., Any])

def logger_ast(func: F) -> F: ...

class NodeLink(NamedTuple):
    level: int
    parent: Union[ast.FunctionDef, ast.ClassDef, ast.Module]

class NodeDef(NamedTuple):
    title: str
    definition: str
    docstring: str
    level: int
    def get_summary(self) -> str: ...
    def get_toc_elem(self) -> str: ...
    def get_title(self) -> str: ...
    def get_definition(self) -> str: ...
    def get_docstring(self) -> str: ...

class ClassDef(NodeDef):
    def __new__(cls, *args: Any, **kwargs: Any) -> ClassDef: ...
    def __init__(self, title: str, definition: str, docstring: str, level: int) -> None: ...

class FuncDef(NodeDef):
    def __new__(cls, *args: Any, **kwargs: Any) -> FuncDef: ...
    def __init__(self, title: str, definition: str, docstring: str, level: int) -> None: ...
    def get_docstring(self) -> str: ...

class ModuleDef(NodeDef):
    def __new__(cls, *args: Any, **kwargs: Any) -> ModuleDef: ...
    def __init__(self, title: str, definition: str, docstring: str, level: int) -> None: ...

class ObjVisitor(ast.NodeVisitor):
    def __init__(self, module_docstring: bool = ..., priv: bool = ...) -> None: ...
    @property
    def node_lst(self) -> deque[Union[ModuleDef, ClassDef, FuncDef, None]]: ...
    @staticmethod
    def get_tree(source: str) -> ast.AST: ...
    def visit_Module(self, node: ast.Module) -> None: ...
    def visit_ClassDef(self, node: ast.ClassDef) -> None: ...
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None: ...