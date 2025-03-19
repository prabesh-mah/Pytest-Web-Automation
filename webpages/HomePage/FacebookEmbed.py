from webpages.BasePage import BasePage
from webpages.BaseLocators import HomepageLocator
from selenium.webdriver.common.by import By
import time


class FacebookEmbedLocator:
    iframe = (By.XPATH, "//iframe[@title='fb:page Facebook Social Plugin']")
    fb_page_link_inside_iframe = (
        By.XPATH, "//a[normalize-space()='NEPSE ALPHA']")
    close_button = (By.XPATH, "//div[@aria-label='Close']")
    element_to_move = (By.XPATH, "//h4[@class='box_header' and contains(text(),'Nepse Alpha Facebook Page')]")


class FacebookEmbedSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_and_switch_to_frame(self):
        return super().check_and_switch_to_frame(FacebookEmbedLocator.iframe)

    def click_facebook_link_inside_iframe(self):
        self.click(FacebookEmbedLocator.fb_page_link_inside_iframe)

    def click_close_button(self):
        self.click(FacebookEmbedLocator.close_button)

    def homepage_element_is_present(self):
        self.check_element(HomepageLocator.nepse_alpha_fb_page)

