from webpages.BasePage import BasePage
from webpages.BaseLocators import CopyRightLocator
from selenium.webdriver.common.by import By
import time


class CopyrightSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def copyright_verfication(self, text):
        return self.is_text_visible(CopyRightLocator.copyright_symbol_and_text, text)

