from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_header =(By.XPATH, "//h6[normalize-space()='Dashboard']")
        self.time_at_work_widget = (By.XPATH, "//p[normalize-space()='Time at Work']")

    def is_dashboard_displayed(self):
        return self.is_displayed(self.dashboard_header)

    def is_time_widget_displayed(self):
        return self.is_displayed(self.time_at_work_widget)