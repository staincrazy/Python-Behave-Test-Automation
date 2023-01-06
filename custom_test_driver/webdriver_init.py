from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class TestWebDriver:

    @staticmethod
    def chromedriver_setup():

        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument('--disable-notifications')

        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

        return driver
