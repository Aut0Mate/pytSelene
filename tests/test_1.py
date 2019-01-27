from selene import browser


def test_selene_driver_init():
    browser.open_url("http://www.google.com")
    assert 'Google' in browser.title()


def test_selene_2():
    browser.open_url("http://www.google.com")
    assert 'Google' in browser.title()
