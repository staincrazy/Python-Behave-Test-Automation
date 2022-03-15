from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import logging
import os
from datetime import datetime


# Printing out in a console time when test execution starts

def before_all(context):
    print(f"Test execution starts at {datetime.now()}")


# Setting up logger
def before_feature(context, feature):
    print(f'\n Before feature:\n {feature.name}')
    context.logger = logging.getLogger('orange_hrm_tests')
    file_handler = logging.FileHandler('orange_hrm_tests.log')
    file_handler.setFormatter(logging.Formatter())
    context.logger.addHandler(file_handler)
    context.logger.setLevel(logging.DEBUG)


# Setting up WebDriver Manager for Google Chrome browser
def before_scenario(context, scenario):
    print(f'This action is executed before {scenario.name}\n')
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


# Setting up the screenshots for all tests
# and storing test execution result in logs

def after_scenario(context, scenario):
    context.logger.debug(f'{scenario.name} is executed with the following result {scenario.status}')
    screenshot_name = f'{scenario.name} exec at {datetime.now()} with {scenario.status} result .png'
    context.driver.save_screenshot('./screenshots/' + screenshot_name)
    context.driver.quit()


def after_feature(context, feature):
    print('All scenarios executed\n Quitting webdriver')


def after_all(context):
    print(f"Test execution ends at f{datetime.now()}")
