from webpages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class MoveToTopLocator:
    move_to_top_button = (By.XPATH, "//a[@id='back-top']")
    body_tag = (By.TAG_NAME, "body")


class MoveToTop(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_end_of_page(self):
        body = self.check_element(MoveToTopLocator.body_tag)
        if body is None:
            raise Exception("Failed to locate the body tag")
        else:
            body.send_keys(Keys.END)

    def is_move_to_top_button_visible(self):
        element = self.driver.find_element(
            *MoveToTopLocator.move_to_top_button)
        if element.is_displayed():
            print("Move to top button is visible.")
            return True
        else:
            print("Move to top button isn't visible.")
            return False

    def click_movetotop_button(self):
        if self.is_move_to_top_button_visible():
            self.click(MoveToTopLocator.move_to_top_button)
        else:
            assert self.is_move_to_top_button_visible(), "Move to Top button is not visible."

