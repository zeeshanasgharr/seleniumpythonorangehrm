import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_login_valid_user(driver,base_url,credentials):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.open(base_url)
    login_page.login(credentials["username"],credentials["password"])

    #Assertions after Successful Login

    assert dashboard_page.is_dashboard_displayed(),"Dashboard is not displayed after login"
    assert dashboard_page.is_time_widget_displayed(), "Time at Work Widget not Visible"