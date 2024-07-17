import time
import pytest
from selenium import webdriver
from utilities import ReadConfig
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchFrameException, TimeoutException, NoSuchElementException


@pytest.fixture(scope="function")
def browser_call(request):

    # Read file inside of 'config.ini' from ReadConfig utlity
    baseURL = ReadConfig.read_configuration("config file", "base_url")
    browserType = ReadConfig.read_configuration("config file", "browser_type")

    # Initialize Webdriver
    driver = None

    try:
        if browserType == "chrome":
            driver = uc.Chrome()
        elif browserType == "firefox":
            driver = webdriver.Firefox()
        elif browserType == "edge":
            driver = webdriver.Edge()
        else:
            pytest.skip("Unsupported browser!")

    except Exception as e:
        print(f"Error occurred while launching the browser: {str(e)}")

    driver.maximize_window()

    driver.get(baseURL)

    # Wait until 'header_carousel' news is visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='caroufredsel_wrapper_vertical_carousel']")))

    # Passing driver to class level
    request.cls.driver = driver

    yield driver
    driver.close()
