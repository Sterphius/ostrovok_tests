import allure
from allure_commons.types import Severity
import pytest
import os

from tests.Mobile.app.ostrovok_app import ostrovok_app


@allure.tag('Mobile')
@allure.label('owner', 'Sterphius')
@allure.feature('Mobile')
@allure.story('Hotel search')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize('city', ['Moscow'])
@pytest.mark.parametrize('results_count', [2])
def test_hotel_search_results_for_popular_city(city, results_count):
    ostrovok_app.skip_auth()\
        .location_input_click()\
        .choose_city_from_popular(city)\
        .search_button_click()\
        .results_are_visible(results_count)


@allure.tag('Mobile')
@allure.label('owner', 'Sterphius')
@allure.feature('Mobile')
@allure.story('User login')
@allure.severity(Severity.CRITICAL)
def test_login():
    email = os.getenv('TEST_USER_EMAIL')
    password = os.getenv('TEST_USER_PASSWORD')

    ostrovok_app.click_login_button()\
        .login_user(email=email, password=password)\
        .user_is_logged_in(email=email)


@allure.tag('Mobile')
@allure.label('owner', 'Sterphius')
@allure.feature('Mobile')
@allure.story('Support')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize('results_count', [2])
def test_support(results_count):
    ostrovok_app.skip_auth()\
        .support_nav_button_click()\
        .support_phone_call_click()\
        .at_least_support_number_results_appeared(results_count)
