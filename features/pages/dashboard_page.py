from features.pages.base_page import BasePage


class DashboardPageLocators:
    dashboard_page_tab = ".//a[@id='menu_dashboard_index']"


class DashboardPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )
