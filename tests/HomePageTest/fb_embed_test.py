from webpages.HomePage.FacebookEmbed import FacebookEmbedSection
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.timeout(50)
@pytest.mark.medium_priority
class TestFacebookEmbed(BaseTest):

    @pytest.mark.order(19)
    def test_facebook_embed_visibility_and_interactivity_on_homepage(self):
        fb_embed = FacebookEmbedSection(self.driver)
        main_tab = self.driver.current_window_handle  # save baseurl
        self.driver.execute_script("window.scrollBy(0, 5500);")
        fb_embed.check_and_switch_to_frame()
        fb_embed.click_facebook_link_inside_iframe()
        fb_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_tab)
        fb_embed.click_close_button()
        expected_url = "https://www.facebook.com/nepsealpha/?ref=embed_page"
        assert self.driver.current_url == expected_url, f"URL doesn't match"
        self.driver.close()
        self.driver.switch_to.window(main_tab)
        fb_embed.homepage_element_is_present()
        assert self.driver.current_url == "https://www.nepsealpha.com/", f"URL doesn't match"
