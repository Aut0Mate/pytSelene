import os
import time
from time import sleep

from PIL import Image
from selene import browser
from selene.conditions import exist
from selene.support.jquery_style_selectors import s
from selenium.webdriver.common.by import By

from definitions import SCREENSHOTS_DIR, TESTS_DIR
from utils.general_utils.logger import Logger

log = Logger(__file__).log


def wait(time_to_wait: float=0.5):
    """
    Calls the time.sleep() for provided time_to_wait
    :param time_to_wait:
    :return:
    """
    sleep(time_to_wait)


def is_element_present(locator: By):
    """
    Verifies if an element is present in the dom
    :param locator:
    :return:
    """
    try:
        s(locator).should(exist, 5)
        return True
    except Exception as e:
        log.info(">>>> ", e)
        return False


def capture_screenshot(filename: str):
    """
    Captures screen-shot with the provided filename and puts in the screenshots directory under reports directory
    :param filename:
    :return:
    """
    log.info("Capturing failure screenshot " + filename)
    browser.take_screenshot(path=SCREENSHOTS_DIR, filename=filename)
    return True


def get_test_file_path(test_file: str):
    """
    Returns absolute path to the test_file
    :param test_file:
    :return:
    """
    return os.path.join(TESTS_DIR, test_file)


def take_full_page_screenshot(filename: str):
    """
    Takes the screen-shot of the entire WebPage and saves with the filename passed as argument
    :param filename:
    :return:
    """
    log.debug("Starting the full page screen-shot utility...")
    total_width = browser.execute_script("return document.body.offsetWidth")
    total_height = browser.execute_script("return document.body.parentNode.scrollHeight")
    viewport_width = browser.execute_script("return document.body.clientWidth")
    viewport_height = browser.execute_script("return window.innerHeight")
    log.debug("Total: ({}, {}), Viewport: ({}, {})".format(total_width, total_height, viewport_width, viewport_height))

    browser.execute_script("window.scrollTo(0, 0)")
    patches = []

    captured_height = 0
    while captured_height < total_height:
        captured_width = 0
        current_height = captured_height + viewport_height

        if current_height > total_height:
            current_height = total_height

        while captured_width < total_width:
            current_width = captured_width + viewport_width

            if current_width > total_width:
                current_width = total_width

            log.debug("Appending to the patches ({}, {}, {}, {})".format(captured_width, captured_height, current_width,
                                                                         current_height))
            patches.append((captured_width, captured_height, current_width, current_height))

            captured_width += viewport_width

        captured_height += viewport_height

    final_image = Image.new('RGB', (total_width, total_height))
    previous = None
    part = 0

    for patch in patches:
        if previous:
            browser.execute_script("window.scrollTo({0}, {1})".format(patch[0], patch[1]))
            log.debug("Scrolled to {}, {}".format(patch[0], patch[1]))
            time.sleep(0.2)

        file_name = "part_{}.png".format(part)
        log.info("Capturing {} ...".format(file_name))

        browser.take_screenshot(path=SCREENSHOTS_DIR, filename=file_name[:-4])
        file_name = os.path.join(SCREENSHOTS_DIR, file_name)
        screen_shot = Image.open(file_name)

        if patch[1] + viewport_height > total_height:
            offset = (patch[0], total_height - viewport_height)
        else:
            offset = (patch[0], patch[1])

        log.debug("Adding to stitched image with offset ({0}, {1})".format(offset[0], offset[1]))
        final_image.paste(screen_shot, offset)

        del screen_shot

        os.remove(file_name)
        part += 1
        previous = patch

    final_image.save(os.path.join(SCREENSHOTS_DIR, filename))
    log.debug("Full page screen_shot workaround complete...")
    return True


class SoftAssert:

    """
    This is an attempt to implement soft assert (verify), since it is not available in pytest.

    using soft assert class methods the script execution will not stop on an assert failure, instead will be added to
    the failures list.

    In the end the assert_all method can be used to assert the list with an empty list
    """

    def __init__(self):
        self._errors = []

    def assert_equals(self, actual, expected, failure_message=None):
        """
        Soft assert if 2 objects are equal
        :param actual:
        :param expected:
        :param failure_message:
        :return:
        """
        if not failure_message:
            failure_message = "Expected [%s] but found [%s]" % (expected, actual)
        if actual != expected:
            self._errors.append("[%s != %s]. " % (actual, expected) + failure_message)

    def assert_true(self, expression, failure_message):
        """
        Soft assert if the expression is True
        :param expression:
        :param failure_message:
        :return:
        """
        if not expression:
            self._errors.append(failure_message)

    def assert_all(self):
        """
        Assert all soft asserts
        :return:
        """
        assert self._errors == [], '\n' + ('\n'.join(self._errors))
