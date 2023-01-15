import logging
from docstring2md.__config__ import LOGGING_MSG as LOGGING_MSG, LOGGING_SETUP as LOGGING_SETUP

logger: logging.Logger

def define_logfile(path: str) -> None: ...
