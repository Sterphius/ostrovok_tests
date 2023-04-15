import os

import allure
import pytest
from allure_commons.types import Severity

from tests.UI.data.cities import cities
from tests.UI.data.user import User
from tests.UI.pages.ostrovok_main import main_page
from tests.UI.pages.resources import lang_symbol, lang_title


@allure.tag('UI', 'WEB')
@allure.feature('UI')
class TestWebUI:

    @allure.story('Search')
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.parametrize("city", cities)
    def test_simple_search(self, city):
        main_page.given_opened()
        main_page.fill_destination(value=city, autocomplete=True)
        main_page.results_found(timeout=10, count=20)

    @allure.story('Login')
    @allure.severity(Severity.BLOCKER)
    def test_login(self):
        email = os.getenv('TEST_USER_EMAIL')
        password = os.getenv('TEST_USER_PASSWORD')

        test_user = User(email=email, password=password)

        main_page.given_opened()
        main_page.login_user(test_user)
        main_page.user_is_logged_in(test_user)

    @allure.story('Language')
    def test_change_lang(self):
        main_page.given_opened()
        main_page.check_html_language(lang_symbol[main_page.language])

    @allure.story('Main page')
    @allure.severity(Severity.BLOCKER)
    def test_check_title_with_lang(self):
        main_page.given_opened()
        main_page.title_has_text(lang_title[main_page.language])

    @allure.story('Currency')
    @allure.severity(Severity.BLOCKER)
    def test_change_currency(self, prepare_new_currency):
        currency = prepare_new_currency
        main_page.given_opened()
        main_page.find_and_choose_currency(currency=currency, language=main_page.language, choose=True)
        main_page.should_have_currency(currency=currency)

    @allure.story('Currency')
    def test_find_fake_currency(self):
        main_page.given_opened()
        main_page.find_and_choose_currency('fake', language=main_page.language, choose=False)
        main_page.currency_not_found_text_appeared(main_page.language)
