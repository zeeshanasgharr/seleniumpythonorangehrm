from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_input=(By.NAME,"username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def open(self,base_url):
        self.navigate_to(base_url)

    def enter_username(self,username):
        self.send_keys(self.username_input, username)

    def enter_password(self,password):
        self.send_keys(self.password_input, password)

    def click_login_button(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()


