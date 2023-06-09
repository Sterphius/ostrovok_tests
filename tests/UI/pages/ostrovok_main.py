import os

import allure

from selene import browser, have

from tests.UI.data.user import User
from tests.UI.pages.locators import destination_input, search_button, user_email_input, user_password_input, \
    sign_in_button, login_control, currency_widget, currency_widget_code, progress_bar, hotel_search_list
from tests.UI.pages.resources import currency_not_found_texts, currency_placeholder


def get_current_language():
    current_lang = browser.element('[class^="LanguageWidget-module__value"]') \
        .locate() \
        .get_attribute('textContent')
    return current_lang


class OstrovokMainPage:

    def __init__(self):
        self.language = None
        self.currency = None

    def given_opened(self):
        with allure.step('Open main page'):
            browser.open(os.getenv('OSTROVOK_WEB_URL'))
            self.language = get_current_language()
        return self

    def fill_destination(self, value: str, autocomplete: bool = False):
        with allure.step(f'Type city {value} and click search'):
            if autocomplete:
                destination_input \
                    .type(value)\
                    .press_enter()
            else:
                destination_input \
                    .type(value)
            search_button.click()
        return self

    def login_user(self, user: User):
        with allure.step(f'Login user with credentials'):
            login_control.click()
            user_email_input.type(user.email)
            user_password_input.type(user.password)
            sign_in_button.click()
        return self

    def user_is_logged_in(self, user: User):
        with allure.step(f'Check that user with {user.email} is logged in'):
            login_control.should(have.text(user.email))
        return self

    def find_and_choose_currency(self, currency: str, language: str, choose: bool = False):
        with allure.step(f'Find currency {currency} in language {language}'):
            currency_widget.click()
            selector = f'[class^="Input-module__control"][placeholder="{currency_placeholder[language]}"]'
            browser.element(selector).set_value(currency)
        with allure.step(f'Choose currency {currency} from list'):
            if choose:
                currency_widget_code.element_by(have.text(currency)).click()
        return self

    def get_current_currency(self):
        with allure.step(f'Get current currency'):
            self.currency = browser.element('[class^="CurrencyWidget-module__value"]').locate() \
                .get_attribute("textContent").split(',')[0]
        return self

    def should_have_currency(self, currency):
        with allure.step(f'Check that current currency is {currency}'):
            browser.element('[class^="CurrencyWidget-module__value"]').should(have.text(currency))
        return self

    def currency_not_found_text_appeared(self, language):
        with allure.step(f'Currency not found text appeared in {language}'):
            browser.element('[class^=CurrencyWidget-module__result]')\
                .should(have.text(currency_not_found_texts[language]))
        return self

    def results_found(self, timeout: int, count: int):
        with allure.step(f'Find at least {count} hotel results in {timeout} seconds'):
            progress_bar.with_(timeout=timeout)
            hotel_search_list.should(have.size_greater_than_or_equal(count))
        return self

    def title_has_text(self, text: str):
        with allure.step(f'Main page title contains {text}'):
            browser.element('.homepage-howdy-title').should(have.text(text))
        return self

    def check_html_language(self, language):
        with allure.step(f'Check that html lang set to {language}'):
            browser.element('html').should(have.attribute('lang').value(language))
        return self


main_page = OstrovokMainPage()
