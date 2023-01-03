from docstring2md.file import MyFile as MyFile
from typing import NamedTuple

class DocString2MDOptions(NamedTuple):
    toml: MyFile
    uml: MyFile
    export_file: MyFile
    toc: bool
    private_def: bool

class DocString2MD:
    def __init__(self, module_name: str, options: DocString2MDOptions) -> None: ...
    def import_module(self) -> int: ...
    def get_doc(self) -> str: ...
    def writedoc(self) -> int: ...
