from behave import *

from features.pages.dashboard_page import DashboardPage, DashboardPageLocators
from features.pages.login_page import LoginPageLocators, LoginPage

use_step_matcher("re")


@given('I navigate to "(?P<application_url>.+)"')
def navigate_to_application(context, application_url):
    context.driver.get(application_url)
    # verifying that no redirection was performed
    try:
        assert context.driver.current_url == "".format(LoginPageLocators.application_url)
    except AssertionError:
        print("Either redirection was performed, or condition is not correct")
        print(context.driver.current_url)


@then('I see proper "(?P<page_title>.+)"')
def verify_page_title(context, page_title):
    assert page_title == LoginPageLocators.login_page_title


@when('I enter login "(?P<login>.+)"')
def enter_login(context, login):
    login_page = LoginPage(context)
    login_page.enter_login(login)


@step("I click on login button")
def click_on_login_button(context):
    login_page = LoginPage(context)
    login_page.click_on_login_button()


@then("I see dashboard")
def verify_dashboard_visible(context):
    dashboard_page = DashboardPage(context)
    dashboard_page.is_visible(DashboardPageLocators.dashboard_page_tab)


@step('I enter password "(?P<password>.+)"')
def enter_password(context, password):
    login_page = LoginPage(context)
    login_page.enter_password(password)
