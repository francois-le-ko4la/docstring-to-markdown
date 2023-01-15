from docstring2md.__config__ import LOGGING_MSG as LOGGING_MSG
from docstring2md.ast_engine import NodeListType as NodeListType, ObjVisitor as ObjVisitor
from docstring2md.file import MyFile as MyFile
from docstring2md.log import logger as logger

class PytMod:
    def __init__(self, module_name: str, priv: bool = ...) -> None: ...
    @property
    def module(self) -> str: ...
    @property
    def node_lst(self) -> NodeListType: ...
    @property
    def pkg_main_docstring(self) -> NodeListType: ...
    def ismodule(self) -> bool: ...
    def read(self) -> None: ...