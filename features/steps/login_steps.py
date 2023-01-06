from behave import *
from features.pages.dashboard_page import DashboardPageSelectors
from features.pages.login_page import LoginPageSelectors

use_step_matcher("re")


@given('I navigate to "(?P<application_url>.+)"')
def navigate_to_application(context, application_url):
    context.browser.navigate(application_url)


@then('I see proper "(?P<page_title>.+)"')
def verify_page_title(context, page_title):

    try:
        assert page_title == context.browser.get_page_title()
    except AssertionError:
        print(f"Test fails for expected title - {page_title} whilst "
              f"actual page title is {context.browser.get_page_title()}")


@when('I enter username "(?P<username>.+)"')
def enter_login(context, username):
    context.browser.input_text(LoginPageSelectors.LOGIN_FIELD, username)


@step('I enter password "(?P<password>.+)"')
def enter_password(context, password):
    context.browser.input_text(LoginPageSelectors.PASSWORD_FIELD, password)


@step("I click on login button")
def click_on_login_button(context):
    context.browser.click(LoginPageSelectors.LOGIN_BUTTON)


@then("I see dashboard")
def verify_dashboard_visible(context):
    assert context.browser.is_visible(DashboardPageSelectors.DASHBOARD_PAGE_TAB)
