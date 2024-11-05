from webpages.HomePage.APkDownload import APKDownloadSection
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestAPKDownloadRedirection(BaseTest):

    @pytest.mark.order(22)
    @pytest.mark.timeout(60)
    @pytest.mark.medium_priority
    def test_apk_download(self):
        apk_download = APKDownloadSection(self.driver)
        main_tab = self.driver.current_window_handle  # save current window
        apk_download.click_apk_download_icon()
        time.sleep(2)
        self.driver.switch_to.window(
            self.driver.window_handles[1])  # switch gdrive tab | 1
        apk_download.apk_name_element_presence_on_gdrive_tab()
        apk_download.click_download_icon_on_gdrive()
        time.sleep(2)
        self.driver.switch_to.window(
            self.driver.window_handles[2])  # switch download tab | 2
        apk_download.apk_download_element_presence_on_download_page()
        apk_download.click_download_button()
        time.sleep(18)

        # Close all other tabs except main
        for handle in self.driver.window_handles:
            if handle != main_tab:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(main_tab)

        apk_download.validate_download()
