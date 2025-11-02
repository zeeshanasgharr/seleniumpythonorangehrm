import time

from pages.login_page import LoginPage


def test_login_valid_user(driver,base_url,credentials):
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(credentials["username"],credentials["password"])