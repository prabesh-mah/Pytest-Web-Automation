from webpages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class MoveToTopLocator:
    header_news_carousel = (
        By.XPATH, "//div[@class='caroufredsel_wrapper_vertical_carousel']")
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

    def click_movetotop_button(self):
        self.click(MoveToTopLocator.move_to_top_button)

    def header_news_carousel_element(self):
        element = self.check_element(MoveToTopLocator.header_news_carousel)
        if element is None:
            raise Exception(
                f"Failed to locate element with locator '{element}'")
        else:
            return element
