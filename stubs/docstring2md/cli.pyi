import argparse
from docstring2md import __script_descr__ as __script_descr__, __script_epilog__ as __script_epilog__
from docstring2md.__config__ import ARG_HIGHLIGHT as ARG_HIGHLIGHT, ARG_STYLE as ARG_STYLE, CHK_PYT_MIN as CHK_PYT_MIN, CONST as CONST, EX_CONFIG as EX_CONFIG, EX_OK as EX_OK, LOGGING_MSG as LOGGING_MSG
from docstring2md.doc2md import DocString2MD as DocString2MD, DocString2MDOptions as DocString2MDOptions
from docstring2md.file import MyFile as MyFile
from docstring2md.log import define_logfile as define_logfile, logger as logger

def check_python() -> bool: ...
def get_argparser() -> argparse.ArgumentParser: ...
def run() -> int: ...
