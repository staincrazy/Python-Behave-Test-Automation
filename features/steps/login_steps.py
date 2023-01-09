from behave import *

from engine.custom_test_driver import browser
from features.pages.dashboard_page import DashboardPageSelectors
from features.pages.login_page import LoginPageSelectors

use_step_matcher("re")


@given('I navigate to "(?P<application_url>.+)"')
def navigate_to_application(context: {browser}, application_url: str) -> None:
    context.browser.navigate(application_url)


@then('I see proper "(?P<page_title>.+)"')
def verify_page_title(context: {browser}, page_title: str) -> None:
    try:
        assert page_title == context.browser.get_page_title()
    except AssertionError:
        print(f"Test fails for expected title - {page_title} whilst "
              f"actual page title is {context.browser.get_page_title()}")


@when('I enter username "(?P<username>.+)"')
def enter_login(context: {browser}, username: str) -> None:
    context.browser.input_text(LoginPageSelectors.LOGIN_FIELD, username)


@step('I enter password "(?P<password>.+)"')
def enter_password(context: {browser}, password: str) -> None:
    context.browser.input_text(LoginPageSelectors.PASSWORD_FIELD, password)


@step("I click on login button")
def click_on_login_button(context: {browser}) -> None:
    context.browser.click(LoginPageSelectors.LOGIN_BUTTON)


@then("I see dashboard")
def verify_dashboard_visible(context: {browser}) -> None:
    assert context.browser.is_visible(DashboardPageSelectors.DASHBOARD_PAGE_TAB)
