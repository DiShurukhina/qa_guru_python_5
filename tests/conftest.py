import pytest
from selene.support.shared import config, browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    config.base_url = 'https://demoqa.com'
    config.window_height = 1080
    config.window_width = 1920
    yield
    browser.quit()