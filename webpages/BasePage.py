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
        """ Clicks on an element specified by the locator. """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"ERROR: Unable to click on element with locator '{
                locator}'. Exception: {e}")
            raise

    def type(self, locator, keyword):
        """ Types a given keyword into an input field specified by the locator. """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.send_keys(keyword)
        except (NoSuchElementException, TimeoutException) as e:
            print(f"ERROR: Unable to type '{keyword}' into element with locator '{
                locator}'. Exception: {e}")
            raise

    def locate_element(self, locator):
        """ Locates and returns an element specified by the locator. """
        try:
            element = self.driver.find_element(*locator)
            return element
        except NoSuchElementException as e:
            print(f"ERROR: Unable to find element with locator '{
                locator}'. Exception: {e}")
            raise

    def take_screenshot(self, name="screenshot"):
        """ Takes a screenshot of the current browser window and saves it to a file. """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"

        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_path = os.path.join(screenshot_dir, screenshot_name)

        try:
            self.driver.save_screenshot(screenshot_path)
        except Exception as e:
            print(f"ERROR: Failed to take screenshot. Exception: {e}")

    def check_element(self, locator):
        """ Checks for the presence of an element specified by the locator. """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"ERROR: Element with locator '{
                locator}' is not present. Exception: {e}")
            raise

    def check_elements(self, locator):
        """ Checks for the presence of multiple elements specified by the locator. """
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            print(f"ERROR: Elements with locator '{
                locator}' are not present. Exception: {e}")
            raise

    def is_logo_visible(self, locator):
        """ Checks if the logo specified by the locator is visible. """
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except (TimeoutException, NoSuchElementException) as e:
            print(
                f"ERROR: Logo not found or not visible within the timeout period. Exception: {e}")
            raise

    def is_text_visible(self, locator, text):
        """ Checks if a specific text is visible within an element specified by the locator. """
        try:
            return text in self.wait.until(EC.visibility_of_element_located(locator)).text
        except (NoSuchElementException, TimeoutException) as e:
            print(
                f"ERROR: Element not found or text not visible within the timeout period. Exception: {e}")
            raise

    def get_element_text(self, locator):
        """ Retrieves and returns the text from an element specified by the locator. """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator))
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            print(
                f"ERROR: Unable to retrieve text from element within the timeout period. Exception: {e}")
            raise

    def get_element_text_with_index(self, locator, index):
        """ Retrieves and returns the text from an element at a specific index specified by the locator. """
        try:
            elements = self.driver.find_elements(*locator)
            if index < len(elements):
                return elements[index].text
            else:
                print(f"WARNING: Index '{
                    index}' is out of range for elements with locator '{locator}'.")
                return None
        except (TimeoutException, NoSuchElementException) as e:
            print(f"ERROR: Unable to retrieve elements with locator '{
                locator}'. Exception: {e}")
            raise

    def move_to_element(self, locator):
        """ Moves to an element specified by the locator using ActionChains. """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator))
            self.actions.move_to_element(element).perform()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"ERROR: Unable to move to element with locator '{
                locator}'. Exception: {e}")

    def move_to_element_and_click(self, locator):
        """ Moves to an element and clicks it using ActionChains. """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator))
            self.actions.move_to_element(element).click().perform()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"ERROR: Unable to hover and click on element with locator '{
                locator}'. Exception: {e}")

    def check_and_switch_to_frame(self, locator):
        """ Checks for a frame specified by the locator and switches to it. """
        try:
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it(locator))
        except (NoSuchFrameException, TimeoutException) as e:
            print(f"ERROR: Unable to switch to frame with locator '{
                locator}'. Exception: {e}")

    def move_to_element_using_js(self, locator):
        """ Scrolls to an element specified by the locator using JavaScript. """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator))
            self.driver.execute_script(
                "arguments[0].scrollIntoView();", element)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"ERROR: Unable to scroll to element with locator '{
                locator}'. Exception: {e}")

    def scroll_using_js(self, origin):
        """ Scrolls the window vertically by a specified amount using JavaScript. """
        self.driver.execute_script(f"window.scrollBy(0, {origin});")

    def scroll_to_top_using_js(self):
        """ Scrolls the window to the top using JavaScript. """
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_end_using_js(self):
        """ Scrolls the window to the bottom using JavaScript. """
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def get_attribute(self, locator, attribute):
        """ Retrieves and returns the value of a specified attribute from an element. """
        try:
            return self.wait.until(EC.presence_of_element_located(locator)).get_attribute(attribute)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"ERROR: Unable to retrieve attribute '{
                attribute}' from element with locator '{locator}'. Exception: {e}")
            raise

    def len_of_direct_child_element(self, locator):
        """ Returns the number of direct child elements for a parent specified by the locator. """
        try:
            parent_element = self.wait.until(
                EC.visibility_of_element_located(locator))
            # Optional wait; consider removing or adjusting based on your needs.
            time.sleep(1)
            direct_child_elements = WebDriverWait(parent_element, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, "./*")))
            print(f"INFO: Number of direct child elements for '{
                locator}': {len(direct_child_elements)}")
            return len(direct_child_elements)
        except NoSuchElementException as e:
            print(f"ERROR: Parent element with locator '{
                locator}' not found. Exception: {e}")
            return 0
