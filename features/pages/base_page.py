from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):

        self.driver = driver

    def click(self, by_locator):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def clear(self, by_locator):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def assert_element_text_equals(self, by_locator, element_text):

        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return web_element.text == element_text

    def input_text(self, by_locator, text):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self, by_locator):

        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def is_visible(self, by_locator):

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
