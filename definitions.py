# All Project directory paths are listed here as constants
from os.path import join as stitch
import os
import sys

# Add Current Working Directory to sys.path
sys.path.append(os.getcwd())

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Project Root
DRIVERS_DIR = stitch(ROOT_DIR, 'drivers')
CONFIGS_DIR = stitch(ROOT_DIR, 'configurations')
LOGGING_CONFIG_FILE = stitch(CONFIGS_DIR, 'logging.ini')
LOGS_DIR = stitch(ROOT_DIR, 'logs')
LOG_FILE = stitch(LOGS_DIR, 'selenium.log')
TEST_DATA_DIR = stitch(ROOT_DIR, 'test_data')
TESTS_DIR = stitch(ROOT_DIR, 'tests')
TESTS_DIR_REL = '../tests/'
TEST_SUITES_DIR = stitch(ROOT_DIR, 'test_suites')
REPORTS_DIR = stitch(ROOT_DIR, 'reports')
REPORTS_DIR_REL = '../reports/'
SCREENSHOTS_DIR = stitch(ROOT_DIR, 'screenshots')
