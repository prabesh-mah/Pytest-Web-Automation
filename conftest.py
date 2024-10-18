from selenium import webdriver
from utilities import ReadConfig
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import os


@pytest.fixture(scope="function")
def setup_and_teardown(request):

    # Read file inside of 'config.ini' from ReadConfig utlity
    baseURL = ReadConfig.read_configuration("config file", "base_url")
    browserType = ReadConfig.read_configuration("config file", "browser_type")

    # Access Browserstack token key from environment variable
    browserstack_token = os.getenv('browserstack_token')

    # Initialize Webdriver
    driver = None

    if browserType == "chrome":
        driver = uc.Chrome()
    elif browserType == "firefox":
        driver = webdriver.Firefox()
    elif browserType == "edge":
        driver = webdriver.Edge()
    elif browserType == "safari":
        safari_options = webdriver.SafariOptions()
        capabilities = {
            'browserName': 'Safari',
            'browser_version': 'latest',
            'os': 'macOS',
            'os_version': 'Sonoma',
            'name': 'Selenium Test'
        }

        # Create a remote WebDriver instance using BrowserStack
        driver = webdriver.Remote(
            command_executor=f'https://wickedman_tW4Iy0:{
                browserstack_token}@hub-cloud.browserstack.com/wd/hub',
            options=safari_options
        )
    else:
        pytest.fail(f"Unsupported browser type: '{
            browserType}'. Supported browsers are: 'chrome', 'firefox', 'edge'.")

    # Maximize window and open the base URL
    driver.maximize_window()
    driver.get(baseURL)

    # Wait for a specific element to be visible after the page loads
    homepage_element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, "//img[@src='/images/logo.jpg']")))

    assert "nepsealpha" in driver.current_url

    # Sharing WebDriver instance across all test methods in a class
    request.cls.driver = driver

    yield driver
    driver.quit()


'''
# Enable this for cross browser testing
@pytest.fixture(params=['chrome', 'edge', 'firefox'])
def setup_and_teardown(request):

    # Read file inside of 'config.ini' from ReadConfig utlity
    baseURL = ReadConfig.read_configuration("config file", "base_url")
    browserType = ReadConfig.read_configuration("config file", "browser_type")

    # Initialize Webdriver
    driver = None

    if request.param == "chrome":
        driver = uc.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        pass

    # Maximize window and open the base URL
    driver.maximize_window()
    driver.get(baseURL)

    # Wait for a specific element to be visible after the page loads
    homepage_element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, "//img[@src='/images/logo.jpg']")))

    assert "nepsealpha" in driver.current_url

    # Sharing WebDriver instance across all test methods in a class
    request.cls.driver = driver

    yield driver
    driver.quit()
'''
