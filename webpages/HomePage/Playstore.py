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

        text = "We're sorry, the requested URL was not found on this server."

        visible_text = self.is_text_visible(
            PlaystoreLocator.error_text, text)

        if self.is_text_visible(
                PlaystoreLocator.error_text, text):

            print(f"PASSED! Visibility of text is: {visible_text}")
        else:
            print(f"FAILED! Visibility of text is: {visible_text}")
