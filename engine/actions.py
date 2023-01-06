from custom_test_driver import Browser

browser = Browser()


def click(selector):

    browser.click(selector)


def input_text(selector, text):

    browser.input_text(selector, text)


def navigate(url):

    browser.navigate(url)


def get_url():

    return browser.get_current_url()


def get_title():

    return browser.get_page_title()


def is_visible(selector):

    return browser.is_visible(selector)