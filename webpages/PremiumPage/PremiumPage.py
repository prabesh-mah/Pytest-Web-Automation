from webpages.BasePage import BasePage
from webpages.BaseLocators import NavigationMenuLocator
from selenium.webdriver.common.by import By
import time


class PremiumPageLocators:

    element = (By.XPATH, "//h2[normalize-space()='Our Payment Vendors']")
    khalti_button = (By.XPATH, "//button[normalize-space()='Khalti']")
    esewa_button = (By.XPATH, "//button[normalize-space()='eSewa']")
    connect_ips_button = (
        By.XPATH, "//button[normalize-space()='Connect IPS']")


class PremiumPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_premium(self):
        self.click(NavigationMenuLocator.premium_button)

    def click_khalti_button(self):
        self.click(PremiumPageLocators.khalti_button)

    def click_esewa_button(self):
        self.click(PremiumPageLocators.esewa_button)

    def click_connect_ips_button(self):
        self.click(PremiumPageLocators.connect_ips_button)