from pages.BaseApp import BasePage

class RegHelper(BasePage):

    def enter_data_in_field(self, input_date, locator):
        input_field = self.find_element(locator)
        input_field.send_keys(input_date)
        return input_field

    def find_error(self, locator):
        return self.find_element(locator).get_attribute('innerText')

    def click_btn(self, locator):
        return self.find_element(locator).click()
