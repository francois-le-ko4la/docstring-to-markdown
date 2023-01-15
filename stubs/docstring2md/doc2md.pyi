from docstring2md.__config__ import CONST as CONST, EX_OK as EX_OK, EX_OSFILE as EX_OSFILE, TAG as TAG
from docstring2md.file import MyFile as MyFile
from docstring2md.mod import PytMod as PytMod
from typing import NamedTuple

class DocString2MDOptions(NamedTuple):
    toml: MyFile
    uml: MyFile
    todo: MyFile
    output: MyFile
    toc: bool
    private_def: bool

class DocString2MD:
    def __init__(self, module_name: str, options: DocString2MDOptions) -> None: ...
    def import_module(self) -> int: ...
    def get_doc(self) -> str: ...
    def writedoc(self) -> int: ...
