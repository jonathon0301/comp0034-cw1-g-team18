import time
from basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = BasePage(
        webdriver.Chrome(executable_path='/comp0034-cw1-g-team18/test/chromedriver_mac_arm64/chromedriver'))
    yield driver
    driver.quit()


def test_click_elements(driver):
    driver.get("http://localhost:8050/")
    time.sleep(15)
    fruit_s = driver.find_elements(By.CSS_SELECTOR, "#histogram-selector label input")
    for fruiti in fruit_s:
        fruiti.click()

    driver.find_element(By.CSS_SELECTOR, '#xaxis_selector').click()
    for x_axis_selector in range(1, 4):
        time.sleep(2)
        x_axis = '.VirtualizedSelectOption:nth-child({})'.format(x_axis_selector)
        driver.find_element(By.CSS_SELECTOR, x_axis).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '#yaxis_selector').click()
        for y_axis_selector in range(1, 4):
            time.sleep(2)
            y_axis = '.VirtualizedSelectOption:nth-child({})'.format(y_axis_selector)
            driver.find_element(By.CSS_SELECTOR, y_axis).click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '#yaxis_selector').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '#xaxis_selector').click()

    driver.find_element(By.CSS_SELECTOR, '#map_selector').click()
    for map_selector in range(1, 4):
        time.sleep(2)
        map = '.VirtualizedSelectOption:nth-child({})'.format(map_selector)
        driver.find_element(By.CSS_SELECTOR, map).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '#map_selector').click()

    driver.find_element(By.CSS_SELECTOR, '#bar_selector').click()
    for bar_selector in range(1, 4):
        time.sleep(2)
        bar = '.VirtualizedSelectOption:nth-child({})'.format(bar_selector)
        driver.find_element(By.CSS_SELECTOR, bar).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '#bar_selector').click()
