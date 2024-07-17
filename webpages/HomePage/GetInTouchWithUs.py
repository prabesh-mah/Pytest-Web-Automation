from webpages.BasePage import BasePage
from webpages.BaseLocators import HomepageLocator
from selenium.webdriver.common.by import By
import time


class GetInTouchWithUsLocator:
    get_in_touch_with_us = (By.XPATH, "//h4[text()='Get In Touch With Us']")
    facebook_button = (By.XPATH, "//a[@title='Nepse Alpha Facebook Page']")
    close_dialog_button_fb = (By.XPATH, "//div[@aria-label='Close']")
    x_button = (By.XPATH, "//a[@title='Nepse Alpha Twitter Page']")
    close_dialog_button_x = (By.XPATH, "//div[@aria-label='Close']")
    youtube_button = (By.XPATH, "//a[@title='Nepse Alpha Youtube Channel']")
    youtube_element = (By.XPATH, "//a[normalize-space()='nepsealpha.com']")


class GetInTouchWithUsSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_facebook_button(self):
        self.click(GetInTouchWithUsLocator.facebook_button)

    def click_close_button_on_fb_dialog_box(self):
        self.click(GetInTouchWithUsLocator.close_dialog_button_fb)

    def click_x_button(self):
        self.click(GetInTouchWithUsLocator.x_button)

    def click_close_button_on_x_dialog_box(self):
        self.click(GetInTouchWithUsLocator.close_dialog_button_x)

    def click_youtube_button(self):
        self.click(GetInTouchWithUsLocator.youtube_button)

    def check_youtube_element(self):
        self.check_element(GetInTouchWithUsLocator.youtube_element)

    def move_to_about_nepse_alpha(self):
        self.check_element(HomepageLocator.about_nepse_alpha)
