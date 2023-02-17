from pages.BaseApp import BasePage
from locators import AuthPageLocators


class LoginHelper(BasePage):

    def enter_accounting_data(self, ac_date):
        input_field = self.find_element(AuthPageLocators.USER_NAME)
        input_field.click()
        input_field.send_keys(ac_date)
        return input_field

    def enter_pass(self, pass_data):
        input_field = self.find_element(AuthPageLocators.PASSWORD)
        input_field.click()
        input_field.send_keys(pass_data)
        return input_field

    def choose_phone(self):
        self.find_element(AuthPageLocators.TAB_PHONE).click()

    def choose_email(self):
        return self.find_element(AuthPageLocators.TAB_EMAIL).click()

    def choose_login(self):
        return self.find_element(AuthPageLocators.TAB_LOGIN).click()

    def choose_account(self):
        return self.find_element(AuthPageLocators.TAB_ACCOUNT).click()

    def click_on_the_login_button(self):
        return self.find_element(AuthPageLocators.BTN_LOGIN).click()

    def find_text(self, locator):
        return self.find_element(locator).get_attribute('innerText')

    def hide_pass(self):
        self.find_element(AuthPageLocators.BTN_HIDE).click()
        return self.find_element(AuthPageLocators.PASSWORD).get_attribute('type')
