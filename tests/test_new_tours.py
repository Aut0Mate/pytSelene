from __init__ import *
import pytest
from selene import browser
from selene.bys import by_xpath

from definitions import REPORTS_DIR, TESTS_DIR, TEST_DATA_FILE
from page_objects.new_tours_home_page import *
from utils.general_utils.excel_utils import get_data_from_excel_for_parameterize
from utils.general_utils.gen_utils import SoftAssert

test_register_user_args = get_data_from_excel_for_parameterize(TEST_DATA_FILE, "test_register_user")


@pytest.mark.parametrize(test_register_user_args[0], test_register_user_args[1])
def test_register_user(first_name, last_name, phone, email, address1, address2, city, state, postal_code, country,
                       user_name,
                       password, confirm_password):
    browser.open_url("http://newtours.demoaut.com/")
    click_register_link()
    register_user(f_name=first_name, l_name=last_name, number=phone, email=email, address1=address1, address2=address2,
                  city=city, state=state, postal_code=postal_code, country=country, user_name=user_name,
                  password=password, confirm_password=confirm_password)


def test_all_links():
    browser.open_url("http://newtours.demoaut.com/")
    sa = SoftAssert()
    s(by_xpath("//a[.='SIGN-OFF']")).click()
    sa.assert_equals(browser.title(), "Sign-on: Mercury Tours", "The browser title for Sign on page did not match")
    s(by_link_text("SUPPORT")).click()
    sa.assert_equals(browser.title(), "Under Construction: Mercury Tour",
                     "The browser title for Support page did not match")
    s(by_link_text("REGISTER")).click()
    sa.assert_equals(browser.title(), "Register: Mercury Tour",
                     "The browser title for Support page did not match")
    sa.assert_all()


if __name__ == '__main__':
    pytest.main(['--html=' + REPORTS_DIR + os.sep + 'test_new_tours_report.html',
                 '--self-contained-html', '-v', '-q', '-s', os.path.join(TESTS_DIR, 'test_new_tours.py')])
