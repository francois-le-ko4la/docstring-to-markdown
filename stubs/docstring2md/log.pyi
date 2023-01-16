import logging
from docstring2md.__config__ import LOGGING_SETUP as LOGGING_SETUP, LOG_MSG as LOG_MSG

logger: logging.Logger

def define_logfile(path: str) -> None: ...
