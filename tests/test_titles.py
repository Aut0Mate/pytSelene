import os
import sys
import pytest
from selene import browser
from selene.conditions import visible
from selene.support.jquery_style_selectors import s
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), os.pardir))
from definitions import REPORTS_DIR_REL, TESTS_DIR, ROOT_DIR


def test_google_title():
    browser.open_url("http://www.google.com")
    assert 'Google' in browser.title()


def test_quora_title():
    browser.open_url("https://www.quora.com/")
    assert 'Quora' in browser.title()


def test_wiki_title():
    browser.open_url("https://www.wikipedia.com/")
    assert 'wiki' in browser.title(), "[wiki] not found in Title: " + browser.title()


def test_selene_assert():
    browser.open_url("https://www.wikipedia.com/")
    s("ImNotThere").should_be(visible)


if __name__ == '__main__':
    sys.path.append(os.path.join(os.getcwd(), os.pardir))
    sys.path.append(ROOT_DIR)

    print('PYTHON PATH: ' + str(sys.path))
    pytest.main(['--html=' + REPORTS_DIR_REL + 'title_tests_report.html',
                 '--self-contained-html', '-v', '-q', '-s', os.path.join(TESTS_DIR, 'test_titles.py')])
