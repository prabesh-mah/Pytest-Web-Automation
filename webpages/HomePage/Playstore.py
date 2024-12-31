from webpages.BasePage import BasePage
from selenium.webdriver.common.by import By


class PlaystoreLocator:
    playstore_download_icon = (By.XPATH, "//img[@src='/images/android.png']")
    error_text = (
        By.XPATH, "//div[@id='error-section' and contains(text(),'requested URL was not found on this server')]")

    # New Update
    playstore_text = (
        By.XPATH, "//span[contains(text(),'Nepsealpha NEPSE app Portfolio')]")


class PlaystoreSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_playstore_icon(self):
        self.click(PlaystoreLocator.playstore_download_icon)

    def is_nepse_alpha_text_visible_on_playstore(self):
        expected_text = 'Nepsealpha NEPSE app Portfolio'

        if self.is_text_visible(PlaystoreLocator.playstore_text, expected_text):
            print(f"The app name text matches the: {
                expected_text}")
        else:
            assert False, f"The app name text doesn't matches the: {
                expected_text}"
