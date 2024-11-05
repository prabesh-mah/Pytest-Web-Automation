from webpages.HomePage.Playstore import PlaystoreSection
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestPlaystoreRedirection(BaseTest):

    @pytest.mark.order(18)
    @pytest.mark.timeout(30)
    @pytest.mark.high_priority
    def test_playstore_redirection(self):
        playstore = PlaystoreSection(self.driver)
        main_tab = self.driver.current_window_handle  # save current window
        playstore.click_playstore_icon()
        playstore_tab = self.driver.window_handles[1]  # save playstore page
        self.driver.switch_to.window(playstore_tab)

        expected_name = 'Nepsealpha NEPSE app Portfolio'

        playstore_text_matches = playstore.playstore_verfication(
            expected_name)
        if playstore_text_matches:
            print(f"Redirects to Nepsealpha Playstore Page: {
                expected_name}")
        else:
            assert False, f"Failed to Redirect to Nepsealpha Playstore Page: {
                expected_name}"

        self.driver.close()
        self.driver.switch_to.window(main_tab)
