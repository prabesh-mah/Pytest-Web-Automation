from webpages.BasePage import BasePage
from webpages.BaseLocators import HomepageLocator
from selenium.webdriver.common.by import By
import time


class AboutNepseAphaLocator:
    address = (
        By.XPATH, "//p[contains(normalize-space(),'Krishna Galli') and contains(normalize-space(),'Pulchowk') and contains(normalize-space(),'Lalitpur 44700')]")
    mobile_num = (
        By.XPATH, "//a[contains(normalize-space(),'+977-9813667733')]")
    landline_num = (By.XPATH, "//a[text()='01-5919211']")
    email_address = (
        By.XPATH, "//a[contains(normalize-space(),'info@nepsealpha.com')]")


class AboutNepseAphaSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def move_to_element_using_js(self):
        return super().move_to_element_using_js(HomepageLocator.about_nepse_alpha)

    def is_address_visible_and_correct(self):
        expected_address = "Krishna Galli\nPulchowk,\nLalitpur 44700"
        if self.is_text_visible(AboutNepseAphaLocator.address, expected_address):
            print(
                f"The address matches the:\n{expected_address}")
        else:
            assert False, f"The address does not match the:\n{
                expected_address}"

    def is_mobile_num_visible_and_correct(self):
        expected_contact = "+977-9813667733"
        if self.is_text_visible(AboutNepseAphaLocator.mobile_num, expected_contact):
            print(f"The mobile num matches the:\n{expected_contact}")
        else:
            assert False, f"The mobile num does not match the:\n{
                expected_contact}"

    def is_landline_num_visible_and_correct(self):
        expected_contact = "01-5919211"
        if self.is_text_visible(AboutNepseAphaLocator.landline_num, expected_contact):
            print(f"The landline matches the:\n{expected_contact}")
        else:
            assert False, f"The landline does not match the:\n{
                expected_contact}"
