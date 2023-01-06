from datetime import datetime

from engine.custom_test_driver.browser import Browser
from engine.custom_test_driver.webdriver_init import TestWebDriver
from utilities.logger import TestLogger


def before_all(context): pass


def before_feature(context, feature):

    # Setting up logger
    context.logger = TestLogger.get_logger()


def before_scenario(context, scenario):

    # Setting up webdriver
    context.browser = Browser(TestWebDriver.chromedriver_setup())


def after_scenario(context, scenario):

    context.logger. \
        debug(f'{scenario.name} is executed with the result {scenario.status} at {datetime.now()}')

    screenshot_name = f'{scenario.name} exec at {datetime.now()} with {scenario.status} result .png'

    context.browser.save_screenshot(screenshot_name)
    context.browser.quit()


def after_feature(context, feature): pass


def after_all(context): pass
