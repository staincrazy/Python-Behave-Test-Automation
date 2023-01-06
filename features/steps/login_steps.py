from behave import *
from engine.actions import *
from features.pages.dashboard_page import DashboardPageSelectors
from features.pages.login_page import LoginPageSelectors

use_step_matcher("re")


@given('I navigate to "(?P<application_url>.+)"')
def navigate_to_application(context, application_url):
    navigate(application_url)


@then('I see proper "(?P<page_title>.+)"')
def verify_page_title(context, page_title):
    assert page_title == get_title()


@when('I enter username "(?P<username>.+)"')
def enter_login(context, username):
    input_text(LoginPageSelectors.LOGIN_FIELD, username)


@step('I enter password "(?P<password>.+)"')
def enter_password(context, password):
    input_text(LoginPageSelectors.PASSWORD_FIELD, password)


@step("I click on login button")
def click_on_login_button(context):
    click(LoginPageSelectors.LOGIN_BUTTON)


@then("I see dashboard")
def verify_dashboard_visible(context):
    assert is_visible(DashboardPageSelectors.DASHBOARD_PAGE_TAB)
