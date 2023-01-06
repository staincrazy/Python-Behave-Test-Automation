from selenium.webdriver.common.by import By


class LoginPageSelectors:

    APPLICATION_URL = "https://opensource-demo.orangehrmlive.com/index.php"
    LOGIN_PAGE_TITLE = "OrangeHRM"
    LOGIN_FIELD = (By.XPATH, ".//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, ".//button[@type='submit']")
