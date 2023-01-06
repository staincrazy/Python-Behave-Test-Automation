from selenium.webdriver.common.by import By


class LoginPageSelectors:

    APPLICATION_URL = "https://opensource-demo.orangehrmlive.com/index.php"
    LOGIN_PAGE_TITLE = "OrangeHRM"
    LOGIN_FIELD = (By.XPATH, ".//input[@id='txtUsername']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@id='txtPassword']")
    LOGIN_BUTTON = (By.XPATH, ".//input[@id='btnLogin']")
