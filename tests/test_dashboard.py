from pages.dashboard_page import DashboardPage

def test_admin_menu_clickable(login_logout, driver):
    dashboard = DashboardPage(driver)
    dashboard.click_admin_menu()
    assert "admin" in driver.current_url.lower(), "Admin page did not open after clicking Admin menu"
