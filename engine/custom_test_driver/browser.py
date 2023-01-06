from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:

    def __init__(self, driver, timeout=None):

        if timeout is not None:
            self.timeout = timeout
        else:
            self.timeout = 10

        self.driver = driver

    def get_page_title(self):

        return self.driver.title

    def get_current_url(self):

        return self.driver.current_url

    def navigate(self, url):

        self.driver.get(url)

    def click(self, by_locator):

        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException:
            return None

    def clear(self, by_locator):

        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).clear()
        except TimeoutException:
            return None

    def assert_element_text_equals(self, by_locator, expected_text):

        web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return web_element.text == expected_text

    def input_text(self, by_locator, text):

        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))\
                .send_keys(text)
        except TimeoutException:
            return None

    def is_enabled(self, by_locator):

        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))

    def is_visible(self, by_locator):

        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))

    def hover_over(self, by_locator):

        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def quit(self):

        self.driver.quit()

    def save_screenshot(self, screenshot_name):

        self.driver.save_screenshot('./screenshots/' + screenshot_name)

