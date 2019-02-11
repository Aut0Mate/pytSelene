from selene.bys import by_link_text
from selene.support.conditions.have import attribute
from selene.support.jquery_style_selectors import s
from selenium.webdriver.support.select import Select

from utils.general_utils.logger import Logger

log = Logger(__file__).log


def click_register_link():
    s(by_link_text("REGISTER")).click()
    s("title").should_have(attribute('text', 'Register: Mercury Tours'), 10)


def enter_first_name(first_name: str):
    s("input[name='firstName']").clear().send_keys(first_name)


def enter_last_name(last_name: str):
    s("input[name='lastName']").clear().send_keys(last_name)


def enter_phone(number: str):
    s("input[name='phone']").clear().send_keys(number)


def enter_email(email: str):
    s("input[name='userName']").clear().send_keys(email)


def enter_mailing_address_line1(address: str):
    s("input[name='address1']").clear().send_keys(address)


def enter_mailing_address_line2(address: str):
    s("input[name='address2']").clear().send_keys(address)


def enter_city(city: str):
    s("input[name='city']").clear().send_keys(city)


def enter_state_or_province(state: str):
    s("input[name='state']").clear().send_keys(state)


def enter_postal_code(postal_code: str):
    s("input[name='postalCode']").clear().send_keys(postal_code)


def select_country(country: str):
    Select(s("select[name='country']")).select_by_visible_text(country.upper())


def enter_user_name(user_name: str):
    s("input[name='email']").clear().send_keys(user_name)


def enter_password(password: str):
    s("input[name='password']").set_value(password)


def enter_in_confirm_password(password: str):
    s("input[name = 'confirmPassword']").set_value(password)


def click_submit():
    s("input[name = 'register']").scroll_to().click()


def register_user(f_name, l_name, number, email, address1, address2, city, state, postal_code, country, user_name,
                  password, confirm_password):
    enter_first_name(first_name=f_name)
    enter_last_name(last_name=l_name)
    enter_phone(number=number)
    enter_email(email=email)
    enter_mailing_address_line1(address=address1)
    enter_mailing_address_line2(address=address2)
    enter_city(city=city)
    enter_state_or_province(state=state)
    enter_postal_code(postal_code=postal_code)
    select_country(country=country)
    enter_user_name(user_name=user_name)
    enter_password(password=password)
    enter_in_confirm_password(password=confirm_password)
    click_submit()
