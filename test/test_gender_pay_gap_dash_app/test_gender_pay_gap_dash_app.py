import time
from basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = BasePage(webdriver.Chrome(executable_path='/comp0034-cw1-g-team18/test/chromedriver_mac_arm64/chromedriver'))


driver.get("http://localhost:8050/")
time.sleep(15)
fruit_s = driver.find_elements(By.CSS_SELECTOR, "#histogram-selector label input")
for fruiti in fruit_s:
    fruiti.click()

driver.find_element(By.CSS_SELECTOR, '#xaxis_selector').click()
for i in range(1, 4):
    time.sleep(2)
    a = '.VirtualizedSelectOption:nth-child({})'.format(i)
    driver.find_element(By.CSS_SELECTOR, a).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#yaxis_selector').click()
    for j in range(1, 4):
        time.sleep(1)
        b = '.VirtualizedSelectOption:nth-child({})'.format(j)
        driver.find_element(By.CSS_SELECTOR, b).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#yaxis_selector').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#xaxis_selector').click()

driver.find_element(By.CSS_SELECTOR, '#map_selector').click()
for c1 in range(1, 4):
    time.sleep(2)
    c = '.VirtualizedSelectOption:nth-child({})'.format(c1)
    driver.find_element(By.CSS_SELECTOR, c).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#map_selector').click()

driver.find_element(By.CSS_SELECTOR, '#bar_selector').click()
for d1 in range(1, 4):
    time.sleep(2)
    d = '.VirtualizedSelectOption:nth-child({})'.format(d1)
    driver.find_element(By.CSS_SELECTOR, d).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#bar_selector').click()

# Quit Browser
driver.quit()