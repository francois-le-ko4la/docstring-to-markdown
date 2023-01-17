from _typeshed import Incomplete
from enum import Enum, IntEnum
from typing import NamedTuple

class Const(Enum):
    DOCSTRING_EMPTY: str
    HEAD_TAG: str
    DEV_HEAD: str
    DEV_TOML: str
    DEV_UML: str
    DEV_OBJ: str
    DECORATOR_TAG: str
    FUNCTION_TAG: str
    PROPERTY_TAG: str
    COMA: str
    DOT: str

class Tag(Enum):
    BEG_END_CO: str
    BEG_MERMAID: str
    BEG_TOML: str
    BEG_PY: str
    BEG_PRE: str
    END_PRE: str
    BEG_STR: str
    END_STR: str
    END_STRH: str
    BEG_B: str
    END_B: str
    END_BH: str
    BEG_TITLE: str
    END_TITLE: str
    SPACE: str
    TAB: str
    HTML_TAB: str
    CR: str
    HTML_CR: str
    QUOTE: str
    COMA: str

class LoggingSetup(NamedTuple):
    logfile: str
    default_level: str
    default_format: str
    simple_format: str
    file_format: str
    encoding: str
    @classmethod
    def set_logfile(cls, path: str) -> LoggingSetup: ...

LOGGING_SETUP: LoggingSetup

class EventMSG(NamedTuple):
    info: str
    warning: str
    error: str
    debug: str

class LogMessages(NamedTuple):
    logfile: EventMSG
    args: EventMSG
    python: EventMSG
    dump: EventMSG
    result: EventMSG
    elapse_time: EventMSG
    pytmod: EventMSG
    pytmod_mod: EventMSG
    pytmod_script: EventMSG
    pytmod_extract: EventMSG
    new_module: EventMSG
    new_class: EventMSG
    new_func: EventMSG
    node_link_analysis_beg: EventMSG
    node_link_analysis_end: EventMSG
    unknown_type_of_node: EventMSG
    io_err: EventMSG
    file_not_found: EventMSG
    write_doc: EventMSG

LOG_MSG: Incomplete
CHK_PYT_MIN: tuple[int, int, int]
ROOT_DIR: str
PID: int

class ExitStatus(IntEnum):
    EX_OK: int
    EX_OSFILE: int
    EX_CANTCREAT: int
    EX_IOERR: int
    EX_CONFIG: int

ARG_STYLE: dict[str, str]
ARG_HIGHLIGHT: list[str]
