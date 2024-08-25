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
            print(f"ERROR: Unable to click on element with locator '{
                  locator}'.")

    def type(self, locator, keyword):
        try:
            self.wait.until(EC.presence_of_element_located(
                locator)).send_keys(keyword)
        except (TimeoutError, NoSuchElementException):
            print(f"ERROR: Unable to type '{
                  keyword}' into element with locator '{locator}'.")

    def check_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutError, NoSuchElementException):
            print(f"ERROR: Element with locator '{locator}' is not present.")
            return None

    def check_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except (TimeoutError, NoSuchElementException):
            print(f"ERROR: Elements with locator '{locator}' are not present.")
            return None

    def is_logo_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except (TimeoutError, NoSuchElementException):
            print("ERROR: Logo not found or not visible within the timeout period.")
            return False

    def is_text_visible(self, locator, text):
        try:
            return text in self.wait.until(EC.visibility_of_element_located(locator)).text
        except (TimeoutError, NoSuchElementException):
            print(
                "ERROR: Element not found or text not visible within the timeout period.")
            return False

    def get_element_text(self, locator):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator))
            return element.text
        except (TimeoutException, NoSuchElementException):
            print(
                "ERROR: Unable to retrieve text from element within the timeout period.")
            return None

    def get_element_text_with_index(self, locator, index):
        try:
            elements = self.driver.find_elements(*locator)
            if index < len(elements):
                return elements[index].text
            else:
                print(f"WARNING: Index '{
                      index}' is out of range for elements with locator '{locator}'.")
                return None
        except (TimeoutException, NoSuchElementException):
            print(f"ERROR: Unable to retrieve elements with locator '{
                  locator}'.")
            return None

    def move_to_element(self, locator):
        try:
            self.actions.move_to_element(self.wait.until(
                EC.visibility_of_element_located(locator))).perform()
        except (TimeoutError, NoSuchElementException):
            print(f"ERROR: Unable to move to element with locator '{
                  locator}'.")

    def move_to_element_and_click(self, locator):
        try:
            self.actions.move_to_element(self.wait.until(
                EC.visibility_of_element_located(locator))).click().perform()
        except (TimeoutError, NoSuchElementException):
            print(f"ERROR: Unable to hover and click on element with locator '{
                  locator}'.")

    def check_and_switch_to_frame(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it(locator))
        except (NoSuchFrameException, TimeoutException):
            print(f"ERROR: Unable to switch to frame with locator '{
                  locator}'.")

    def move_to_element_using_js(self, locator):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.wait.until(
                EC.visibility_of_element_located(locator)))
        except (TimeoutError, NoSuchElementException):
            print(f"ERROR: Unable to scroll to element with locator '{
                  locator}'.")

    def get_attribute(self, locator, attribute):
        try:
            return self.wait.until(EC.presence_of_element_located(locator)).get_attribute(attribute)
        except (TimeoutException, NoSuchElementException):
            print(f"ERROR: Unable to retrieve attribute '{
                  attribute}' from element with locator '{locator}'.")
            return None

    def scroll_using_js(self, origin):
        self.driver.execute_script(f"window.scrollBy(0, {origin});")

    def scroll_to_top_using_js(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_end_using_js(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def len_of_direct_child_element(self, locator):
        try:
            parent_element = self.wait.until(
                EC.visibility_of_element_located(locator))
            time.sleep(1)
            direct_child_elements = WebDriverWait(parent_element, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, "./*")))
            print(f"INFO: Number of direct child elements for '{
                  locator}': {len(direct_child_elements)}")
            return len(direct_child_elements)
        except NoSuchElementException:
            print(f"ERROR: Parent element with locator '{locator}' not found.")
            return 0
