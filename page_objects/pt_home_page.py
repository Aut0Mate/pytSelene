from selene import browser
from selene.bys import by_xpath
from selene.support.jquery_style_selectors import s
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_blog_link():
    s(by_xpath("//a[normalize-space(.)='Blog']")).click()
    WebDriverWait(browser.driver(), 10).until(expected_conditions.title_contains('Blog'))


def click_home_link():
    s(by_xpath("//a[normalize-space(.)='Home']")).click()
    WebDriverWait(browser.driver(), 10).until(expected_conditions.title_contains('PHPTRAVELS'))
