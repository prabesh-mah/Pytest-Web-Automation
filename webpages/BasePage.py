import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException, TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except (NoSuchElementException, TimeoutException):
            print(f"EXCEPTION! Element with locator '{
                  locator}' failed to Click.")

    def type(self, locator, keyword):
        try:
            self.wait.until(EC.presence_of_element_located(
                locator)).send_keys(keyword)
        except (TimeoutError, NoSuchElementException):
            print(f"EXCEPTION! Element with locator '{
                  locator}' failed to type.")

    def check_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutError, NoSuchElementException):
            print(f"EXCEPTION! Element with locator '{
                  locator}' is not present.")
            return None

    def check_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except (TimeoutError, NoSuchElementException):
            print(f"EXCEPTION! Element with locator '{
                  locator}' is not present.")
            return None

    def is_logo_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except (TimeoutError, NoSuchElementException):
            print(
                "FAILED! Element not found or logo not visible within the timeout period.")
            return False

    def is_text_visible(self, locator, text):
        try:
            return text in self.wait.until(EC.visibility_of_element_located(locator)).text
        except (TimeoutError, NoSuchElementException):
            print(
                "FAILED! Element not found or text not visible within the timeout period.")
            return False

    def move_to_element(self, locator):
        try:
            self.actions.move_to_element(self.wait.until(
                EC.visibility_of_element_located(locator))).perform()
        except (TimeoutError, NoSuchElementException):
            print(f"EXCEPTION! Failed to move to element with locator '{
                locator}'.")

    def move_to_element_and_click(self, locator):
        try:
            self.actions.move_to_element(self.wait.until(
                EC.visibility_of_element_located(locator))).click().perform()
        except (TimeoutError, NoSuchElementException):
            print(f"EXCEPTION! Failed to hover and click on element with locator '{
                locator}'.")

    def check_and_switch_to_frame(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it(locator))
        except (NoSuchFrameException, TimeoutException):
            print(f"EXCEPTION! Element with frame locator '{
                  locator}' not found.")

    def move_to_element_using_js(self, locator):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.wait.until(
                EC.visibility_of_element_located(locator)))
        except (TimeoutError, NoSuchElementException):
            print(f"EXCEPTION! Failed to moved over element with locator '{
                locator}'.")

    def get_attribute(self, locator, attribute):
        return self.wait.until(EC.presence_of_element_located(locator)).get_attribute(attribute)

    def scroll_using_js(self, origin):
        self.driver.execute_script(f"window.scrollBy(0, {origin});")

    def scroll_to_top_using_js(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_end_using_js(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def len_of_direct_child_element(self, locator):
        try:
            parent_element = self.wait.until(EC.visibility_of_element_located(
                (locator)))

            time.sleep(1)

            direct_child_elements = WebDriverWait(parent_element, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, "./*")))

            print(f"Number of Direct child elements: {
                  len(direct_child_elements)}")

        except NoSuchElementException:
            print(f"EXCEPTION! Parent element with locator '{
                  locator}' not found.")
