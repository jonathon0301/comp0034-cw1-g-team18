import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Safari()
    yield browser
    browser.close()


def test_example(browser):
    # Launch the web app
    browser.get("http://localhost:8050/")

    # Verify the presence of certain elements on the page
    element = browser.find_element_by_id("h1")
    assert element == "Gender Pay Gap Visualization"
