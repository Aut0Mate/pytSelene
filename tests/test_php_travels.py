import os
import sys

import pytest
from selene.bys import by_text
from selene.conditions import visible

from definitions import REPORTS_DIR, TESTS_DIR
from page_objects.pt_home_page import *

sys.path.append(os.pardir)


def test_blog_link():
    browser.open_url("https://www.phptravels.net/")
    click_blog_link()
    s(by_text("Latest Posts")).should_be(visible)


def test_home_link():
    browser.open_url("https://www.phptravels.net/")
    click_home_link()
    s(by_text("info@phptravels.com")).should_be(visible)


if __name__ == '__main__':
    print('PYTHON PATH: ' + str(sys.path))
    pytest.main(['--html=' + REPORTS_DIR + os.sep + 'test_php_travels_report.html',
                 '--self-contained-html', '-v', '-q', '-s', os.path.join(TESTS_DIR, 'test_php_travels.py')])
