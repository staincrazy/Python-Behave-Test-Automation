from selenium.webdriver.common.by import By
from engine.actions import *


class LoginPageSelectors:

    APPLICATION_URL = "https://opensource-demo.orangehrmlive.com/index.php"
    LOGIN_PAGE_TITLE = "OrangeHRM"
    LOGIN_FIELD = (By.XPATH, ".//input[@id='txtUsername']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@id='txtPassword']")
    LOGIN_BUTTON = (By.XPATH, ".//input[@id='btnLogin']")


class LoginPage:

    __default_username = ""
    __default_password = ""

    @staticmethod
    def login(username=None, password=None):

        input_text(LoginPageSelectors.LOGIN_FIELD, username)
        input_text(LoginPageSelectors.PASSWORD_FIELD, password)
        click(LoginPageSelectors.LOGIN_BUTTON)

