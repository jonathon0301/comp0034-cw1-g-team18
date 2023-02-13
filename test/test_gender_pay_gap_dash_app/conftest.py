import pytest
from basepage import BasePage
from selenium import webdriver

@pytest.fixture
def driver():
    driver = BasePage(
        webdriver.Chrome(executable_path='/comp0034-cw1-g-team18/test/chromedriver_mac_arm64/chromedriver'))
    yield driver
    driver.quit()

