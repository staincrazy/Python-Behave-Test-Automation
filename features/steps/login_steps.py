from behave import *

from features.pages.login_page import LoginPageLocators

use_step_matcher("re")


@given('I navigate to "(?P<application_url>.+)"')
def step_impl(context, application_url):
    context.driver.get(application_url)
    # verifying that no redirection was performed
    try:
        assert context.driver.current_url == "".format(LoginPageLocators.application_url)
    except AssertionError:
        print("Either redirection was performed, or condition is not correct")
        print(context.driver.current_url)


@then('I see proper "(?P<page_title>.+)"')
def step_impl(context, page_title):
    assert page_title == LoginPageLocators.login_page_title
