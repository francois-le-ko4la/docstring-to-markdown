import ast
from collections import deque
from typing import Any, Callable, NamedTuple, TypeVar, Union

F = TypeVar('F', bound=Callable[..., Any])

def logger_ast(func: F) -> F: ...

class NodeLink(NamedTuple):
    level: int
    parent: Union[ast.FunctionDef, ast.ClassDef, ast.Module]

class ModuleDef(NamedTuple):
    docstring: str
    @staticmethod
    def get_toc_elem() -> None: ...
    def get_summary(self): ...
    def get_docstring(self) -> str: ...

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
NodeListType = deque[Union[NodeDef, ModuleDef, None]]

class ObjVisitor(ast.NodeVisitor):
    def __init__(self, module_docstring: bool = ..., priv: bool = ...) -> None: ...
    @property
    def node_lst(self) -> NodeListType: ...
    @staticmethod
    def get_tree(source: str) -> ast.AST: ...
    def visit_Module(self, node: ast.Module) -> None: ...
    def visit_ClassDef(self, node: ast.ClassDef) -> None: ...
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None: ...
