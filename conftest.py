import pytest
import os
from selene import browser

from definitions import SCREENSHOTS_DIR
from utils.driver_utils.init_driver import initialize_driver, quit_driver
from utils.general_utils.gen_utils import take_full_page_screenshot, capture_screenshot
from utils.general_utils.logger import Logger

log = Logger(__file__).log


@pytest.fixture(scope="session", autouse=True)
def driver():
    """
    setupClass and teardownClass
    Fixture to open browser, navigate to app url in setup and quit driver in the teardown
    :return:
    """
    yield initialize_driver()
    quit_driver()


@pytest.fixture(scope="function", autouse=True)
def log_test_details(request):
    """
    Adds loggers to mark start and end of a test
    :param request:
    :return:
    """
    text = " Starting test [" + request.node.name + "] "
    log.info(text.center(61, "="))
    yield
    if request.node.report_call.failed:
        pass
    elif request.node.report_call.passed:
        pass
    elif request.node.report_call.skipped:
        pass
    else:
        pass
    log.info(">>>>>>>>>>>>>>>>>>>>>>>>> " + request.node.report_call.outcome + " <<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info(" [{}] {} ".format(request.node.name, request.node.report_call.outcome).upper().center(61, "="))
    log.info("")


@pytest.fixture(scope='function', autouse=True)
def refresh_page():
    """
    Teardown fixture to refresh the page
    :return:
    """
    yield
    log.info("Refreshing page...")
    browser.driver().refresh()
    log.info("...Done")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    Extends the pytest plugin to take screenshot and embed in the html report when a test fails
    :param item:
    :return:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    # setting the attribute so that it can be accessed from all fixtures. refer to the fixture log_test_details()
    setattr(item, "report_" + report.when, report)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == 'setup':
        xfail =hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")
            file_name = file_name.replace(".py", "_")
            # when the teh command "python test\test_titles.py" is run from the root folder,
            # the report.nodeid is 'test\test_titles.py' instead of 'test_titles.py'
            # This causes the screenshots to be stored in a tests directory under screenshots directory
            # Hence we replace the '/' or '\' by a '_'
            # so that file_name is 'tests_test_titles' instead of 'tests\test_titles'
            file_name = file_name.replace("/", "_")
            file_name = file_name.replace("\\", "_")
            print(":::::::::::::::::::::::::::::::::::::::::::")
            print(file_name)
            print(":::::::::::::::::::::::::::::::::::::::::::")
            if not os.path.exists(SCREENSHOTS_DIR):
                os.mkdir(SCREENSHOTS_DIR, mode=0o777)
            try:
                take_full_page_screenshot(file_name + ".png")
            except Exception as e:
                log.info(e)
                log.info("FAILED TO TAKE FULL SCREEN SHOT")
                capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % os.path.join('screenshots',
                                                                                              file_name + '.png')
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
