from selenium import webdriver
from utilities import ReadConfig
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os

# Create a remote Safari WebDriver instance for BrowserStack.
def create_remote_safari_driver(browserstack_token):
    capabilities = {
        "browserName": "Safari",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Sequoia",
            "browserVersion": "18.1",
            "projectName": "Nepse Alpha"
        }
    }
    safari_options = webdriver.SafariOptions()

    # Combine options and capabilities
    safari_options.set_capability(
        "bstack:options", capabilities["bstack:options"])

    return webdriver.Remote(
        command_executor=f'https://wickedman_tW4Iy0:{
            browserstack_token}@hub-cloud.browserstack.com/wd/hub',
        options=safari_options
    )


# Initialize WebDriver based on the specified browser type.
def initialize_driver(browserType, browserstack_token):
    if browserType == "chrome":
        return uc.Chrome()
    elif browserType == "firefox":
        return webdriver.Firefox()
    elif browserType == "edge":
        return webdriver.Edge()
    elif browserType == "safari":
        return create_remote_safari_driver(browserstack_token)

    pytest.fail(f"Unsupported browser type: '{browserType}'")


# Wait for the homepage element to be visible and assert URL validity.
def wait_for_homepage_element():
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, "//img[@src='/images/logo.jpg']")))
    assert "nepsealpha" in driver.current_url, "Homepage did not load correctly."


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(request):

    global driver

    baseURL = ReadConfig.read_configuration("config file", "base_url")
    browserType = ReadConfig.read_configuration("config file", "browser_type")
    browserstack_token = os.getenv('browserstack_token')

    driver = initialize_driver(browserType, browserstack_token)

    driver.maximize_window()
    driver.get(baseURL)

    wait_for_homepage_element()

    # Share WebDriver instance across all test methods in a class
    request.cls.driver = driver

    yield driver
    driver.quit()
