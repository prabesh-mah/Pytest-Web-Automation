from webpages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ThemeLocators:
    more_tools = (
        By.XPATH, "//button[@class='btn btn-white btn-ouline-dark btn-sm dropdown-toggle']")
    light_dark_toggle = (By.XPATH, "//a[@id='lightDarkToogle']")
    body = (By.TAG_NAME, "body")


class ThemeSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_more_tools(self):
        try:
            self.click(ThemeLocators.more_tools)
        except (NoSuchElementException, TimeoutException):
            print(f"FAILED! Element not clickable")

    def click_toggle_theme(self):
        self.click(ThemeLocators.light_dark_toggle)
