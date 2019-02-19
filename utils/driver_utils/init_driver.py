from selene import browser
from selene.browsers import BrowserName
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.general_utils.logger import Logger

driver: webdriver = None
log = Logger(__file__).log


def initialize_driver(b=BrowserName.CHROME):
    global driver

    if not driver:
        log.info("Driver is None. Initializing [{}] driver".format(b))
        if b == BrowserName.CHROME:
            options = webdriver.ChromeOptions()
            options.add_argument(argument='disable-infobars')
            driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        elif b == BrowserName.FIREFOX:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise Exception("Invalid Browser Name provided")
    log.info("Setting Selene driver")
    browser.set_driver(driver)
    driver.maximize_window()
    return driver


def quit_driver():
    global driver
    log.info("Quitting the driver")
    driver.quit()
    driver = None
    log.info("Driver is None")
