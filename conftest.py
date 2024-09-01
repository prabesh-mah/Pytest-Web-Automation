from selenium import webdriver
from utilities import ReadConfig
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


@pytest.fixture(scope="function")
def setup_and_teardown(request):

    # Read file inside of 'config.ini' from ReadConfig utlity
    baseURL = ReadConfig.read_configuration("config file", "base_url")
    browserType = ReadConfig.read_configuration("config file", "browser_type")

    chromium_options = uc.ChromeOptions()
    extension_paths = [
        "extensions/Buster",
        "extensions/uBlock Origin"
    ]
    chromium_options.add_argument(
        f"--load-extension={','.join(extension_paths)}")
    chromium_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    # chromium_options.add_argument("--headless")
    chromium_options.add_argument("--disable-infobars")
    chromium_options.add_argument("--disable-gpu")
    chromium_options.add_argument("--ignore-certificate-errors")
    chromium_options.add_argument("--disable-extensions")

    firefox_options = webdriver.FirefoxOptions()
    # firefox_options.headless = True
    firefox_options.set_preference(
        "browser.startup.homepage_override.mstone", "ignore")
    firefox_options.set_preference("security.ssl.enable_ocsp_stapling", False)
    firefox_options.set_preference("app.update.enabled", False)

    # Initialize Webdriver
    driver = None

    if browserType == "chrome":
        driver = uc.Chrome(options=chromium_options)
    elif browserType == "firefox":
        driver = webdriver.Firefox(options=firefox_options)
    elif browserType == "edge":
        driver = webdriver.Edge(options=chromium_options)
    else:
        pytest.fail(f"Unsupported browser type: '{
            browserType}'. Supported browsers are: 'chrome', 'firefox', 'edge'.")

    # Maximize window and open the base URL
    driver.maximize_window()
    driver.get(baseURL)

    # Wait for a specific element to be visible after the page loads
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, "//img[@src='/images/logo.jpg']")))

    assert "nepsealpha" in driver.current_url

    # Sharing WebDriver instance across all test methods in a class
    request.cls.driver = driver

    yield driver
    driver.close()


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
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.XPATH, "//img[@src='/images/logo.jpg']")))

    assert "nepsealpha" in driver.current_url

    # Sharing WebDriver instance across all test methods in a class
    request.cls.driver = driver

    yield driver
    driver.close()
'''
