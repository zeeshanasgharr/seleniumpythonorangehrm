from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver=driver
        self.username_input=(By.NAME,"username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def open(self,base_url):
        self.driver.get(base_url)

    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


