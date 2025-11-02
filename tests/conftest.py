import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
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

