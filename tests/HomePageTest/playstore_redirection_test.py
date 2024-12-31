from webpages.HomePage.Playstore import PlaystoreSection
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestPlaystoreRedirection:

    @pytest.mark.order(18)
    @pytest.mark.timeout(30)
    @pytest.mark.high_priority
    def test_playstore_redirection(self):
        playstore = PlaystoreSection(self.driver)
        main_tab = self.driver.current_window_handle  # save current window
        playstore.click_playstore_icon()
        playstore_tab = self.driver.window_handles[1]  # save playstore page
        self.driver.switch_to.window(playstore_tab)
        playstore.is_nepse_alpha_text_visible_on_playstore()
        self.driver.close()
        self.driver.switch_to.window(main_tab)
