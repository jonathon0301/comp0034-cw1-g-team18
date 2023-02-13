import time
from selenium.webdriver.common.by import By


def test_click_elements(driver):
'''
GIVEN the dash created in gender_pay_gap_dash_app.py is opened
WHEN it passes test_click_elements function
THEN Selenium will test the app automatically by clicking every selector in sequence
'''
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
