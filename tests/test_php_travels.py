import os
import sys

from selene.bys import by_text
from selene.conditions import visible

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
