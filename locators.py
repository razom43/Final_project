from selenium.webdriver.common.by import By


class AuthPageLocators(object):
    CARD_CONTAINER = (By.CLASS_NAME, "card-container__content")
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_ACCOUNT = (By.ID, "t-btn-tab-ls")
    USER_NAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "kc-login")
    FORM_ERROR = (By.ID, "form-error-message")
    BTN_REG = (By.ID, "kc-register")
    BTN_HIDE = (By.CLASS_NAME, "rt-eye-icon")
    USER_NAME_TEXT = (By.CSS_SELECTOR, ".tabs-input-container .rt-input--rounded")


class PassportPageLocators(object):
    PHONE_EDIT = (By.ID, "phone_action")
    LAST_NAME_TEXT = (By.CLASS_NAME, "user-name__last-name")
    BTN_EXIT = (By.ID, "logout-btn")


class RegPageLocators(object):
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    # REGION_NAME_INPUT = (By.CLASS_NAME, "rt-input__input rt-input__input--rounded rt-input__input--orange")
    EMAIL_INPUT = (By.ID, "address")
    PASS_INPUT = (By.ID, "password")
    PASS_CONFIRM_INPUT = (By.ID, "password-confirm")
    BTN_REG = (By.NAME, "register")
    ERROR_NAME = (By.CSS_SELECTOR, ".name-container  .rt-input-container__meta")
    ERROR_PHONE_EMAIL = (By.CSS_SELECTOR, ".email-or-phone .rt-input-container__meta")
