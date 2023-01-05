from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class LoginPageSelectors:

    APPLICATION_URL = "https://opensource-demo.orangehrmlive.com/index.php"
    LOGIN_PAGE_TITLE = "OrangeHRM"
    LOGIN_FIELD = (By.XPATH, ".//input[@id='txtUsername']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@id='txtPassword']")
    LOGIN_BUTTON = (By.XPATH, ".//input[@id='btnLogin']")


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

    def enter_login(self, login):

        self.clear(LoginPageSelectors.LOGIN_FIELD)
        self.input_text(LoginPageSelectors.LOGIN_FIELD, login)

    def enter_password(self, password):

        self.clear(LoginPageSelectors.PASSWORD_FIELD)
        self.input_text(LoginPageSelectors.PASSWORD_FIELD, password)

    def click_on_login_button(self):

        self.click(LoginPageSelectors.LOGIN_BUTTON)
