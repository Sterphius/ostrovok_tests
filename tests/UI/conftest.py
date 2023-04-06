import os
import random
import allure
import pytest
from dotenv import load_dotenv
from selene import browser, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.UI.pages.ostrovok_main import get_current_language
from tests.UI.pages.resources import currencies, lang_title
from utils import attachments


@pytest.fixture(scope='function', autouse=False)
def prepare_new_currency():
    with allure.step(f'Prepare new currency, different from current'):
        browser.open('https://www.ostrovok.ru/')
        # There are 2 different values with (and w/o) symbol like
        # Euro, €
        # AED
        current_currency = browser.element('[class^="CurrencyWidget-module__value"]').locate() \
            .get_attribute("textContent").split(',')[0]
        try:
            currencies.remove(current_currency)
        except ValueError:
            pass
        new_currency = random.choice(currencies)
    return new_currency


@pytest.fixture(scope='function', autouse=False)
def change_lang():
    def _change_lang(value: str):
        with allure.step(f'Change language to {value}'):
            current_lang = get_current_language
            if current_lang != value:
                browser.element('[data-testid="language-widget-control"]').click()
                browser.all('[data-testid="language-widget-item"]').element_by(have.text(value)).click()

    return _change_lang


@pytest.fixture(scope='function', autouse=False)
def get_random_language():
    return random.choice(list(lang_title.keys()))


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "99.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attachments.add_html(browser)
    attachments.add_screenshot(browser)
    attachments.add_logs(browser)
    attachments.add_video(browser)

    browser.quit()
