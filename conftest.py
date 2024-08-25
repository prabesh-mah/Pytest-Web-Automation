from selenium import webdriver
from utilities import ReadConfig
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


@pytest.fixture(scope="function")
def browser_call(request):

    # Read file inside of 'config.ini' from ReadConfig utlity
    baseURL = ReadConfig.read_configuration("config file", "base_url")
    browserType = ReadConfig.read_configuration("config file", "browser_type")

    browser_options = uc.ChromeOptions()
    extension_paths = [
        "extensions/Buster",
        "extensions/uBlock Origin"
    ]
    browser_options.add_argument(
        f"--load-extension={','.join(extension_paths)}")
    browser_options.add_argument(
        "--disable-blink-features=AutomationControlled")

    # Initialize Webdriver
    driver = None

    try:
        if browserType == "chrome":
            driver = uc.Chrome(options=browser_options)
        elif browserType == "firefox":
            driver = webdriver.Firefox(options=browser_options)
        elif browserType == "edge":
            driver = webdriver.Edge(options=browser_options)
        else:
            pytest.skip("Unsupported browser!")

    except Exception as e:
        print(f"Error occurred while launching the browser: {str(e)}")

    else:
        # Maximize window and open the base URL
        driver.maximize_window()
        driver.get(baseURL)
        assert "nepsealpha" in driver.current_url

        # Sharing WebDriver instance across all test methods in a class
        request.cls.driver = driver

    finally:
        yield driver
        driver.close()
