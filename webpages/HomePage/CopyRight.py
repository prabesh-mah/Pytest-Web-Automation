from webpages.BasePage import BasePage
from webpages.BaseLocators import CopyRightLocator
from selenium.webdriver.common.by import By
import time


class CopyrightSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def copyright_company_name_text(self, text):
        return self.is_text_visible(CopyRightLocator.copyright_company_text, text)

    def copyright_symbol(self, text):
        return self.is_text_visible(CopyRightLocator.copyright_symbol, text)
