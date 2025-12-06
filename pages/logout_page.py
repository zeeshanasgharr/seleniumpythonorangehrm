from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LogoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.user_dropdown = (By.CSS_SELECTOR, ".oxd-userdropdown-name")
        self.logout_button = (By.XPATH, "//a[normalize-space()='Logout']")

    def open_user_dropdown(self):
        """Clicks the user dropdown menu."""
        self.click(self.user_dropdown)

    def click_logout(self):
        """Clicks the Logout option."""
        self.click(self.logout_button)

    def logout(self):
        """Full logout sequence."""
        self.open_user_dropdown()
        self.click_logout()
