import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def chrome():
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.maximize_window()
    # driver.implicitly_wait(3)
    yield driver
    driver.quit()
