from webpages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
import os


class APKDownloadLocator:
    apk_download_icon = (
        By.CSS_SELECTOR, "img[src='/images/direct-download.png']")
    gdrive_element = (
        By.XPATH, "//div[@data-tooltip-unhoverable='true'][normalize-space()='Nepsealpha_V1.0.1.apk']")
    gdrive_download_icon = (
        By.XPATH, "//body/div[@aria-label='दर्शक देखाउँदै।']/div[@role='toolbar']/div/div/div/div/div[@aria-label='डाउनलोड गर्नुहोस्']/div[1]")
    download_element = (By.XPATH, "//input[@id='uc-download-link']")
    download_icon = (By.XPATH, "//input[@id='uc-download-link']")


class APKDownloadSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_apk_download_icon(self):
        self.click(APKDownloadLocator.apk_download_icon)

    def apk_name_element_presence_on_gdrive_tab(self):
        self.check_element(APKDownloadLocator.gdrive_element)

    def click_download_icon_on_gdrive(self):
        self.click(APKDownloadLocator.gdrive_download_icon)

    def apk_download_element_presence_on_download_page(self):
        self.check_element(APKDownloadLocator.download_element)

    def click_download_button(self):
        self.click(APKDownloadLocator.download_icon)

    def validate_download(self):
        try:
            # Get the username from environment variables
            username = os.getenv('USERNAME')
            print(username)

            # Set the download directory using the retrieved username
            download_directory = fr"C:\Users\Wicked Man\Downloads"

            file_name = "Nepsealpha_V1.0.1.apk"

            file_path = os.path.join(download_directory, file_name)

            # Assert if the file exists
            assert os.path.exists(file_path), f"{
                file_name} not found in the downloads folder."
            print(f"{file_name} has been successfully downloaded.")

        except FileNotFoundError:
            pass
 