import pytest
from selene import browser


@pytest.fixture()
def open_browser():

    browser.driver.maximize_window()
    browser.config.base_url = 'https://demoqa.com/text-box'

    yield browser

    browser.quit()