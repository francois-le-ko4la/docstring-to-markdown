from typing import NamedTuple

class Const(NamedTuple):
    docstring_empty: str
    head_tag: str
    dev_head: str
    dev_toml: str
    dev_uml: str
    dev_obj: str
    decorator_tag: str
    function_tag: str
    property_tag: str
    coma: str
    dot: str

class Tag(NamedTuple):
    beg_co: str
    end_co: str
    beg_mermaid: str
    beg_toml: str
    beg_py: str
    end_py: str
    beg_pre: str
    end_pre: str
    beg_str: str
    end_str: str
    end_strh: str
    beg_b: str
    beg_title: str
    end_title: str
    end_b: str
    end_bh: str
    tab: str
    html_tab: str
    cr: str
    html_cr: str
    quote: str
    coma: str

class LoggingSetup(NamedTuple):
    logfile: str
    default_level: str
    default_format: str
    simple_format: str
    file_format: str
    encoding: str
    @classmethod
    def set_logfile(cls, path: str) -> LoggingSetup: ...

class LoggingMSG(NamedTuple):
    info: str
    warning: str
    error: str
    debug: str

class LoggingMSGCollection(NamedTuple):
    logfile: LoggingMSG
    args: LoggingMSG
    python: LoggingMSG
    dump: LoggingMSG
    result: LoggingMSG
    elapse_time: LoggingMSG
    pytmod: LoggingMSG
    pytmod_mod: LoggingMSG
    pytmod_script: LoggingMSG
    pytmod_extract: LoggingMSG
    new_module: LoggingMSG
    new_class: LoggingMSG
    new_func: LoggingMSG
    node_link_analysis_beg: LoggingMSG
    node_link_analysis_end: LoggingMSG
    unknown_type_of_node: LoggingMSG
    io_err: LoggingMSG
    file_not_found: LoggingMSG
    write_doc: LoggingMSG

CHK_PYT_MIN: tuple[int, int, int]
ROOT_DIR: str
PID: int
EX_OK: int
EX_OSFILE: int
EX_CANTCREAT: int
EX_IOERR: int
EX_CONFIG: int
CONST: Const
TAG: Tag
LOGGING_SETUP: LoggingSetup
LOGGING_MSG: LoggingMSGCollection
ARG_STYLE: dict[str, str]
ARG_HIGHLIGHT: list
