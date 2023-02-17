from pages.AuthorisationtPage import LoginHelper
from pages.PassportPage import PassportInfo
import locators
import constants


def test_auth_phone_num_valid(chrome):
    """
    тест проверки валидной авторизации по номеру телефона
    """
    rt_page = LoginHelper(chrome)                                       # определяем переменную
    rt_page.go_to_site()                                                # открываем страницу
    rt_page.choose_phone()                                              # выбираем ТАБ телефон
    rt_page.enter_accounting_data(constants.PHONE_NUM_VALID)            # вводим номер телефона
    rt_page.enter_pass(constants.PASS_VALID)                            # вводим пароль
    rt_page.click_on_the_login_button()                                 # нажимаем на кнопку войти
    element = PassportInfo(chrome)                                      # определяем переменную
    assert element.pass_page_last_name_text() == constants.LAST_NAME    # проверяем, что вошли
    element.passport_page_exit()


def test_auth_email_valid(chrome):
    """
        тест проверки валидной авторизации по email
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_email()
    rt_page.enter_accounting_data(constants.EMAIL_VALID)
    rt_page.enter_pass(constants.PASS_VALID)
    rt_page.click_on_the_login_button()
    element = PassportInfo(chrome)
    assert element.pass_page_last_name_text() == constants.LAST_NAME
    element.passport_page_exit()


def test_auth_login_valid(chrome):
    """
    тест проверки валидной авторизации по логину
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_login()
    rt_page.enter_accounting_data(constants.LOGIN_VALID)
    rt_page.enter_pass(constants.PASS_VALID)
    rt_page.click_on_the_login_button()
    element = PassportInfo(chrome)
    assert element.pass_page_last_name_text() == constants.LAST_NAME
    element.passport_page_exit()


def test_auth_account_valid(chrome):
    """
    тест проверки валидной авторизации по лицевому счету
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_account()
    rt_page.enter_accounting_data(constants.ACCOUNT_VALID)
    rt_page.enter_pass(constants.PASS_VALID)
    rt_page.click_on_the_login_button()
    element = PassportInfo(chrome)
    assert element.pass_page_last_name_text() == constants.LAST_NAME
    element.passport_page_exit()


def test_auth_phone_num_not_valid(chrome):
    """
    тест проверки невалидной авторизации по номеру телефона
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_phone()
    rt_page.enter_accounting_data(constants.PHONE_NUM_NOT_VALID)
    rt_page.enter_pass(constants.PASS_VALID)
    rt_page.click_on_the_login_button()
    element = LoginHelper(chrome)
    assert element.find_text(locators.AuthPageLocators.FORM_ERROR) == constants.LOGIN_ERROR_TEXT


def test_auth_email_not_valid(chrome):
    """
    тест проверки невалидной авторизации по email
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_email()
    rt_page.enter_accounting_data(constants.EMAIL_NOT_VALID)
    rt_page.enter_pass(constants.PASS_VALID)
    rt_page.click_on_the_login_button()
    element = LoginHelper(chrome)
    assert element.find_text(locators.AuthPageLocators.FORM_ERROR) == constants.LOGIN_ERROR_TEXT


def test_auth_login_not_valid(chrome):
    """
    тест проверки невалидной авторизации по логину
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_login()
    rt_page.enter_accounting_data(constants.LOGIN_NOT_VALID)
    rt_page.enter_pass(constants.PASS_VALID)
    rt_page.click_on_the_login_button()
    element = LoginHelper(chrome)
    assert element.find_text(locators.AuthPageLocators.FORM_ERROR) == constants.LOGIN_ERROR_TEXT


def test_auth_account_not_valid(chrome):
    """
    тест проверки невалидной авторизации по лицевому счету
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_account()
    rt_page.enter_accounting_data(constants.ACCOUNT_NOT_VALID)
    rt_page.enter_pass(constants.PASS_VALID)
    rt_page.click_on_the_login_button()
    element = LoginHelper(chrome)
    assert element.find_text(locators.AuthPageLocators.FORM_ERROR) == constants.LOGIN_ERROR_TEXT


def test_hide_password(chrome):
    """
    тест проверки работы кнопки скрытьия/показа пароля
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    pass_type = rt_page.hide_pass()
    assert pass_type == constants.HIDE_PASS_TEXT
    pass_type = rt_page.hide_pass()
    assert pass_type == constants.HIDE_PASS_PASS


def test_choice_tab_phone(chrome):
    """
    тест проверки переключения таб телефон
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_phone()
    element = LoginHelper(chrome)
    assert element.find_text(locators.AuthPageLocators.USER_NAME_TEXT) == constants.TEXT_PNONE_NUMBER


def test_choice_tab_email(chrome):
    """
    тест проверки переключения таб почта
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_email()
    element = LoginHelper(chrome)
    assert element.find_text(locators.AuthPageLocators.USER_NAME_TEXT) == constants.TEXT_EMAIL


def test_choice_tab_login(chrome):
    """
    тест проверки переключения таб логин
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_login()
    element = LoginHelper(chrome)
    assert element.find_text(locators.AuthPageLocators.USER_NAME_TEXT) == constants.TEXT_LOGIN


def test_choice_tab_account(chrome):
    """
    тест проверки переключения таб лицевой счет
    """
    rt_page = LoginHelper(chrome)
    rt_page.go_to_site()
    rt_page.choose_account()
    element = LoginHelper(chrome)
    assert element.find_text(locators.AuthPageLocators.USER_NAME_TEXT) == constants.TEXT_ACCOUNT
