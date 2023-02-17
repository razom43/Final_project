from pages.BaseApp import BasePage
from locators import PassportPageLocators


class PassportInfo(BasePage):

    def pass_page_last_name_text(self):
        self.find_element(PassportPageLocators.PHONE_EDIT)
        return self.find_element(PassportPageLocators.LAST_NAME_TEXT).get_attribute('innerText')

    def passport_page_exit(self):
        return self.find_element(PassportPageLocators.BTN_EXIT).click()
