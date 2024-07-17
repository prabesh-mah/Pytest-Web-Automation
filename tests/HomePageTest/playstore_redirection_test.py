from webpages.HomePage.Playstore import PlaystoreSection
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.timeout(30)
@pytest.mark.medium_priority
class TestPlaystoreRedirection(BaseTest):

    @pytest.mark.order(18)
    def test_playstore_redirection(self):
        playstore = PlaystoreSection(self.driver)
        main_tab = self.driver.current_window_handle  # save current window
        playstore.click_playstore_icon()
        playstore_tab = self.driver.window_handles[1]  # save playstore page
        self.driver.switch_to.window(playstore_tab)
        time.sleep(2)
        playstore.visibility_of_error_text_on_playstore()
        self.driver.close()
        self.driver.switch_to.window(main_tab)
