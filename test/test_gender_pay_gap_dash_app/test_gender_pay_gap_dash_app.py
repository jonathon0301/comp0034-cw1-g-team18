import time
from basepage import BasePage
from selenium.webdriver.common.by import By


def test_click_elements(driver):
    """
    GIVEN the dash created in gender_pay_gap_dash_app.py is running
    WHEN the home page is loaded
    THEN Selenium will test the app automatically by clicking every selector in sequence
    """
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


def test_h1_text_equals(driver):
    """
    GIVEN the app is running
    WHEN the homepage is available
    THEN the H1 heading element should be "Gender Pay Gap Situations Visualisation Dashboard"
    """
    driver.get("http://localhost:8050/")
    time.sleep(15)
    h1_element = driver.find_element(By.TAG_NAME, "h1")
    h1_text = h1_element.text
    assert h1_text.casefold() == "Gender Pay Gap Situations Visualisation Dashboard".casefold()


def test_box_dropdown_x(driver):
    """
    GIVEN the Dash app is running
    WHEN the home page has loaded
    THEN 'Region' should be the default at x axis dropdown box of bax plots
    """
    driver.get("http://localhost:8050/")
    time.sleep(15)
    driver.implicitly_wait(15)
    assert (
            "Region" in driver.find_element(By.CSS_SELECTOR, '#xaxis_selector').text
    )


def test_box_dropdown_y(driver):
    """
    GIVEN the Dash app is running
    WHEN the home page has loaded
    THEN 'Percentage of Highly Paid Female' should be the default at y axis dropdown box of bax plots
    """
    driver.get("http://localhost:8050/")
    time.sleep(15)
    driver.implicitly_wait(15)
    assert (
            "Percentage of Highly Paid Female" in driver.find_element(By.CSS_SELECTOR, '#yaxis_selector').text
    )


def test_map_dropdown(driver):
    """
    GIVEN the Dash app is running
    WHEN the home page has loaded
    THEN 'Percentage Difference on Hourly Pay' should be the default at dropdown box selector of map
    """
    driver.get("http://localhost:8050/")
    time.sleep(15)
    driver.implicitly_wait(15)
    assert (
            "Percentage Difference on Hourly Pay" in driver.find_element(By.CSS_SELECTOR, '#map_selector').text
    )


def test_bar_dropdown(driver):
    """
    GIVEN the Dash app is running
    WHEN the home page has loaded
    THEN 'Industry' should be the default at dropdown box selector of barchart
    """
    driver.get("http://localhost:8050/")
    time.sleep(15)
    driver.implicitly_wait(15)
    assert (
            "Industry" in driver.find_element(By.CSS_SELECTOR, '#bar_selector').text
    )
