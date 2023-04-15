import allure
from selene import browser, have

from tests.Mobile.app.locators import more_navigation_button, user_email, support_navigation_button, \
    support_phone_call_button, recycler


class OstrovokMobileApp:
    def __init__(self):
        self.navigation = MainNavigation()
        self.search_screen = SearchScreen()
        self.support_screen = SupportScreen()

    def skip_auth(self):
        with allure.step('Skip auth'):
            browser.element('#button_skip').click()
        return self

    def click_login_button(self):
        with allure.step('Click login button'):
            browser.element('#button_login').click()
        return self

    def login_user(self, email, password):
        with allure.step(f'Login user with {email}'):
            browser.element('#text_email').type(email)
            browser.element('#text_password').type(password)
            browser.element('#button_enter').click()
        return self

    def user_is_logged_in(self, email):
        with allure.step(f'Click on more navigation button'):
            # TODO: ask devs for id
            more_navigation_button.click()

        with allure.step(f'User with email {email} is logged in'):
            # TODO: ask devs for id
            user_email \
                .should(have.text(email))
        return self


class MainNavigation:
    def support_nav_button_click(self):
        with allure.step(f'Click support navigation button'):
            # TODO: ask devs for id
            support_navigation_button.click()
        return self


class SupportScreen:
    def support_phone_call_click(self):
        with allure.step(f'Click support phone call button'):
            # TODO: ask devs for id
            support_phone_call_button.click()
        return self

    def at_least_support_number_results_appeared(self, count):
        with allure.step(f'At least support phone numbers appeared'):
            browser.element('#recycler_loyalty') \
                .all('//androidx.recyclerview.widget.RecyclerView/*') \
                .should(have.size_greater_than_or_equal(count))
        return self


class SearchScreen:
    def location_input_click(self):
        with allure.step('Location input click'):
            browser.element('#text_location').click()
        return self

    def choose_city_from_popular(self, value):
        with allure.step(f'Find {value} from popular'):
            browser.element(f"//*[contains(@text, '{value}' )]").click()
        return self

    def search_button_click(self):
        with allure.step('Click search button'):
            browser.element('#search_button').click()
        return self

    def results_are_visible(self, results_count):
        with allure.step(f'At least {results_count} results are visible'):
            # TODO: ask devs for id
            search_count = recycler.all('//androidx.recyclerview.widget.RecyclerView/*')
            search_count.should(have.size_greater_than_or_equal(results_count))
        return self


ostrovok_app = OstrovokMobileApp()
