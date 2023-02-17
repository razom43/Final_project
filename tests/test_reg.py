import pytest
import constants
import locators
from pages.RegPage import RegHelper


@pytest.mark.parametrize("name", constants.LIST_INVALID_NAME)
def test_invalid_first_name_error(chrome, name):
    rt_page = RegHelper(chrome)
    rt_page.go_to_site()
    rt_page.click_btn(locators.AuthPageLocators.BTN_REG)
    rt_page.enter_data_in_field(name, locators.RegPageLocators.FIRST_NAME_INPUT)
    rt_page.click_btn(locators.RegPageLocators.BTN_REG)
    error_txt = rt_page.find_error(locators.RegPageLocators.ERROR_NAME)
    assert error_txt == constants.ERROR_FIRST_LAST_NAME


@pytest.mark.parametrize("name", constants.LIST_INVALID_NAME)
def test_invalid_last_name_error(chrome, name):
    rt_page = RegHelper(chrome)
    rt_page.go_to_site()
    rt_page.click_btn(locators.AuthPageLocators.BTN_REG)
    rt_page.enter_data_in_field(name, locators.RegPageLocators.LAST_NAME_INPUT)
    rt_page.click_btn(locators.RegPageLocators.BTN_REG)
    error_txt = rt_page.find_error(locators.RegPageLocators.ERROR_NAME)
    assert error_txt == constants.ERROR_FIRST_LAST_NAME


@pytest.mark.parametrize("name", constants.LIST_INVALID_EMAIL_PHONE)
def test_invalid_email_phone_error(chrome, name):
    rt_page = RegHelper(chrome)
    rt_page.go_to_site()
    rt_page.click_btn(locators.AuthPageLocators.BTN_REG)
    rt_page.enter_data_in_field(name, locators.RegPageLocators.EMAIL_INPUT)
    rt_page.click_btn(locators.RegPageLocators.BTN_REG)
    error_txt = rt_page.find_error(locators.RegPageLocators.ERROR_PHONE_EMAIL)
    assert error_txt == constants.ERROR_EMAIL_PHONE
