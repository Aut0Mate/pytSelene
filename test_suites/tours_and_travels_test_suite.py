import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))
import pytest

from definitions import REPORTS_DIR
from utils.general_utils.gen_utils import get_test_file_path

homepage_tests = get_test_file_path('test_new_tours.py')
search_tests = get_test_file_path('test_php_travels.py')
report_name = 'Tours and Travels'

if __name__ == '__main__':
    pytest.main(
        ['--html=' + REPORTS_DIR + os.sep + report_name + '.html',
         '--junitxml=' + REPORTS_DIR + os.sep + report_name + '.xml',
         '-s', '-v', '-q', homepage_tests, search_tests])
