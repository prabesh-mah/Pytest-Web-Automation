from webpages.BasePage import BasePage
from selenium.webdriver.common.by import By
from webpages.BaseLocators import HomepageLocator
import time


class CompanyLogoSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_company_logo_visible(self):
        element = self.driver.find_element(*HomepageLocator.company_logo)
        if element.is_displayed():
            print("The logo is visible.")
            return True
        else:
            print("The logo is not visible.")
            return False
