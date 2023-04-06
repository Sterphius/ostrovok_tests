import allure
from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy


class OstrovokMobileApp:
    def __init__(self):
        self.name = 'ru.ostrovok.android'

    def skip_auth(self):
        with allure.step('Skip auth'):
            browser.element((AppiumBy.ID, f'{self.name}:id/button_skip')).click()
        return self

    def location_input_click(self):
        with allure.step('Location input click'):
            browser.element((AppiumBy.ID, f'{self.name}:id/text_location')).click()
        return self

    def choose_city_from_popular(self, value):
        with allure.step(f'Find {value} from popular'):
            browser.element((AppiumBy.XPATH, f"//*[contains(@text, '{value}' )]")).click()
        return self

    def search_button_click(self):
        with allure.step('Click search button'):
            browser.element((AppiumBy.ID, f'{self.name}:id/search_button')).click()
        return self

    def results_are_visible(self, results_count):
        with allure.step(f'At least {results_count} results are visible'):
            # TODO: ask devs for id
            recycler = browser.element((AppiumBy.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                        'android.widget.FrameLayout/android.widget.LinearLayout/'
                                        'android.widget.FrameLayout/android.widget.RelativeLayout/'
                                        'android.widget.LinearLayout/android.widget.FrameLayout[1]/'
                                        'androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/'
                                        'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                                        'androidx.recyclerview.widget.RecyclerView[2]'))
            search_count = recycler.all((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/*"))
            search_count.should(have.size_greater_than_or_equal(results_count))
        return self

    def click_login_button(self):
        with allure.step('Click login button'):
            browser.element((AppiumBy.ID, f'{self.name}:id/button_login')).click()
        return self

    def login_user(self, email, password):
        with allure.step(f'Login user with {email}'):
            browser.element((AppiumBy.ID, f'{self.name}:id/text_email')).type(email)
            browser.element((AppiumBy.ID, f'{self.name}:id/text_password')).type(password)
            browser.element((AppiumBy.ID, f'{self.name}:id/button_enter')).click()
        return self

    def user_is_logged_in(self, email):
        with allure.step(f'Click on more navigation button'):
            # TODO: ask devs for id
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                             '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                             '/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout['
                             '4]')) \
                .click()

        with allure.step(f'User with email {email} is logged in'):
            # TODO: ask devs for id
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                             '.widget.FrameLayout/android.widget.LinearLayout/'
                             'android.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                             '.LinearLayout/android.widget.FrameLayout[1]/'
                             'androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/'
                             'android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/'
                             'android.widget.LinearLayout[1]/android.widget.TextView')) \
                .should(have.text(email))
        return self

    def support_nav_button_click(self):
        with allure.step(f'Click support navigation button'):
            # TODO: ask devs for id
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                             '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                             '/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout['
                             '3]')).click()
        return self

    def support_phone_call_click(self):
        with allure.step(f'Click support phone call button'):
            # TODO: ask devs for id
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                             '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                             '/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout[1]/androidx.viewpager.widget.ViewPager/'
                             'android.widget.FrameLayout/android.widget.LinearLayout/'
                             'androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]')) \
                .click()
        return self

    def at_least_support_number_results_appeared(self, count):
        with allure.step(f'At least support phone numbers appeared'):
            browser.element((AppiumBy.ID, f'{self.name}:id/recycler_loyalty')) \
                .all((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/*')) \
                .should(have.size_greater_than_or_equal(count))
        return self


ostrovok_app = OstrovokMobileApp()
