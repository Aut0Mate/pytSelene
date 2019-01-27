import logging
import os
from logging.config import fileConfig
from definitions import LOGGING_CONFIG_FILE, LOG_FILE


class Logger:

    __instance = None

    def __new__(cls, val):
        if Logger.__instance is None:
            Logger.__instance = object.__new__(cls)
            Logger.__instance.val = val
            fileConfig(LOGGING_CONFIG_FILE)
        cls.log = logging.getLogger(os.path.basename(val))

        # Add the logfileHandler
        fh = logging.FileHandler(filename=LOG_FILE, mode='w')
        fh.setLevel("DEBUG")
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        cls.log.addHandler(fh)

        return Logger.__instance
