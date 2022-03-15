from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class LoginPageLocators:
    application_url = "https://opensource-demo.orangehrmlive.com/index.php"
    login_page_title = "OrangeHRM"
    login_field = (By.XPATH, "")
    password_field = (By.XPATH, "")
    login_button = (By.XPATH, "")


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

    def enter_login(self, login):
        self.clear(LoginPageLocators.login_field)
        self.enter_text(LoginPageLocators.login_field, login)

    def enter_password(self, password):
        self.clear(LoginPageLocators.password_field)
        self.enter_text(LoginPageLocators.password_field, password)

    def click_on_login_button(self):
        self.click(LoginPageLocators.login_button)
