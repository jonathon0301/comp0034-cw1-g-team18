import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.close()


def test_histograms(browser):
    browser.get("http://localhost:8050/")
    time.sleep(5)
    radio_button = browser.find_elements_by_xpath("//input[@type='radio']")[1]
    radio_button.click()
    time.sleep(5)
    graph_title = browser.find_element_by_css_selector(".svg-title-text")
    assert graph_title.text == "Distribution of DiffMedianHourlyPercent"
