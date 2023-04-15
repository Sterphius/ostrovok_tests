from selene import browser

destination_input = browser.element('[data-testid=destination-input]')
search_button = browser.element('[data-testid="search-button"]')
user_email_input = browser.element('[data-testid="user-widget-sign-in-email-input"]')
user_password_input = browser.element('[data-testid="user-widget-sign-in-password-input"]')
sign_in_button = browser.element('[data-testid="user-widget-sign-in-button"]')
login_control = browser.element('[class^=Control-module__control]')
currency_widget = browser.element('[class^=CurrencyWidget-module__control]')
currency_widget_code = browser.all('[class^=CurrencyWidget-module__code]')
progress_bar = browser.element('.zenserpresult-ready')
hotel_search_list = browser.all('.hotel-wrapper')
