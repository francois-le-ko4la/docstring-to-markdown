from collections import deque
from docstring2md.ast_engine import NodeDef as NodeDef
from typing import Union

class PytMod:
    def __init__(self, module_name: str, priv: bool = ...) -> None: ...
    @property
    def module(self) -> str: ...
    @property
    def node_lst(self) -> deque[Union[NodeDef, None]]: ...
    @property
    def pkg_main_docstring(self) -> deque[Union[NodeDef, None]]: ...
    def ismodule(self) -> bool: ...
    def read(self) -> None: ...
