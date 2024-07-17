from webpages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class AdvertiseWithUsLocator:
    adverise_with_us = (By.XPATH, "//h4[text()='ADVERTISE WITH US']")
    email = (By.LINK_TEXT, "info@nepsealpha.com")
    contact = (
        By.XPATH, "//p[contains(normalize-space(),'+977-4414213') and contains(normalize-space(),'9840099042')]")


class AdvertiseWithUsSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_adverise_with_us_element(self):
        self.click(AdvertiseWithUsLocator.adverise_with_us)

    def is_contact_visible_and_correct(self):
        expected_address = "+977-4414213\n9840099042"
        if self.is_text_visible(AdvertiseWithUsLocator.contact, expected_address):
            print(
                f"The contact matches the:\n{expected_address}")
        else:
            print(f"The contact does not match the:\n{expected_address}")

    def is_email_address_visible_and_correct(self):
        expected_contact = "info@nepsealpha.com"
        if self.is_text_visible(AdvertiseWithUsLocator.email, expected_contact):
            print(f"The email matches the:\n{expected_contact}")
        else:
            print(f"The email does not match the:\n{expected_contact}")
