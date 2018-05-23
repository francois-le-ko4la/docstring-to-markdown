#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
import yaml
import logging.config
import logging
import pathlib

YAML_CONF="/logging.yaml"

class PytLog(object):
    def __init__(self):
        path = pathlib.Path(__file__).resolve().parent
        yaml_conf = str(path) + YAML_CONF
        logging.config.dictConfig(yaml.load(open(yaml_conf, 'r')))
        self.__logger = logging.getLogger()

    def debug(self, msg):
        """
        """
        self.__logger.debug(msg)

    def warning(self, msg):
        """
        """
        self.__logger.warning(msg)

    def info(self, msg):
        """
        """
        self.__logger.info(msg)

    def error(self, msg):
        """
        """
        self.__logger.error(msg)

    def set_level(self, sev):
        self.__logger.setLevel(sev)

    def set_debug(self):
        self.set_level(logging.DEBUG)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
