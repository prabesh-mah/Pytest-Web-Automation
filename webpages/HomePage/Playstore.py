from webpages.BasePage import BasePage
from selenium.webdriver.common.by import By


class PlaystoreLocator:
    playstore_download_icon = (By.XPATH, "//img[@src='/images/android.png']")
    error_text = (
        By.XPATH, "//div[@id='error-section' and contains(text(),'requested URL was not found on this server')]")


class PlaystoreSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_playstore_icon(self):
        self.click(PlaystoreLocator.playstore_download_icon)

    def visibility_of_error_text_on_playstore(self):
        self.check_element(PlaystoreLocator.error_text)

        expected_text = "We're sorry, the requested URL was not found on this server."

        if self.is_text_visible(PlaystoreLocator.error_text, expected_text):

            print(f"PASSED! The visibility of text matches the: {
                  expected_text}")
        else:
            print(f"FAILED! The visibility of text does not matches the: {
                  expected_text}")
