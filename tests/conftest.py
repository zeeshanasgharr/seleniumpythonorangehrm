import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from utils.screenshot_utility import ScreenshotUtility

load_dotenv()

@pytest.fixture()
def driver():
     options = Options()

    # Headless Chrome for Jenkins
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture()
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture()
def credentials():
    return {

        "username": os.getenv("APP_USERNAME"),
        "password": os.getenv("APP_PASSWORD")
    }

@pytest.fixture()
def screenshot(driver, request):
    screenshot_util = ScreenshotUtility(driver)
    yield screenshot_util

    # After the test runs, check for failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        test_name = request.node.nodeid
        error_message = "Test Failed"

        # Extract detailed error message if available
        if hasattr(request.node.rep_call, 'longrepr'):
            error_str = str(request.node.rep_call.longrepr)

            # Case 1: AssertionError with message
            if "AssertionError:" in error_str:
                error_message = (
                    error_str.split("AssertionError:")[-1]
                    .strip()
                    .split('\n')[0]
                )

            # Case 2: Other exceptions
            elif error_str:
                lines = error_str.split('\n')
                for line in lines:
                    if (
                        line.strip()
                        and not line.startswith('E ')
                        and len(line.strip()) > 10
                    ):
                        error_message = line.strip()
                        break

        screenshot_util.take_failure_screenshot(test_name, error_message)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture()
def login_logout(driver, base_url, credentials):
    """
    Logs into the application before a test,
    and logs out automatically after the test.
    """
    login_page = LoginPage(driver)
    logout_page = LogoutPage(driver)

    # --- Login ---
    login_page.open(base_url)
    login_page.login(credentials["username"], credentials["password"])

    # Allow test to run while logged in
    yield login_page

    # --- Logout (runs after test completes) ---
    try:
        logout_page.logout()
    except Exception:
        # If logout fails (e.g., test ended on error), ignore so teardown doesn't break
        pass
