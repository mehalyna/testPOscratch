"""
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""
import pytest
from selenium.webdriver import Chrome

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.fixture
def browser():
   driver = Chrome()
   driver.implicitly_wait(10)
   yield driver
   driver.quit()


def test_basic_duckduckgo_search(browser):
    # Set up some test case data
    PHRASE = 'panda'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE