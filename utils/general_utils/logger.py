import logging
import os
from configparser import ConfigParser
from logging.config import fileConfig

from definitions import LOGGING_CONFIG_FILE, LOG_FILE


class Logger:

    __instance = None

    def __new__(cls, val):
        if Logger.__instance is None:
            Logger.__instance = object.__new__(cls)
            Logger.__instance.val = val
            config = ConfigParser()
            config.read(LOGGING_CONFIG_FILE)
            # writing the 'path to log file' on the fly, to logging.ini since pytest can run from anywhere in the
            # project.
            # putting '../logs/selenium.log' in ini will create 'path not found' exception if pytest not run from root
            # folder
            # hence adding the calculated Logfile path to logging.ini

            # If the 'path to log file' contains '\v' then it is getting converted to 'x0b' when fileConfig is parsing
            # it and raising an exception
            # so need to escape it
            if r'\v' in LOG_FILE:
                path = LOG_FILE.replace(r'\v', r'\\v')
            else:
                path = LOG_FILE
            config['handler_logfileHandler']['args'] = "('" + path + "', 'w')"

            # writing to logging.ini
            with open(LOGGING_CONFIG_FILE, 'w') as configfile:
                config.write(configfile)

            # parse the logging.ini config
            fileConfig(LOGGING_CONFIG_FILE)
        cls.log = logging.getLogger(os.path.basename(val))
        return Logger.__instance
