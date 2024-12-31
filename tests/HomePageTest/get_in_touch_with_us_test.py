from webpages.HomePage.GetInTouchWithUs import GetInTouchWithUsSection
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.timeout(70)
@pytest.mark.medium_priority
class TestGetInTouchWithUs:

    @pytest.mark.order(14)
    @pytest.mark.xfail(reason="validated with url which might fail as it can changes quickly")
    def test_verify_twitter_button_redirects_to_twitter_page(self):
        touch_with_us = GetInTouchWithUsSection(self.driver)
        touch_with_us.move_to_about_nepse_alpha()
        time.sleep(1)
        main_tab = self.driver.current_window_handle  # save default page
        touch_with_us.click_x_button()
        time.sleep(1)
        x_tab = self.driver.window_handles[1]  # save x tab
        self.driver.switch_to.window(x_tab)  # switch to x tab
        time.sleep(2)
        assert self.driver.current_url == "https://x.com/nepse_alpha"
        self.driver.close()  # close fb tab
        self.driver.switch_to.window(main_tab)  # switch to default page

    @pytest.mark.order(15)
    def test_verify_facebook_button_redirects_to_facebook_page(self):
        touch_with_us = GetInTouchWithUsSection(self.driver)
        main_tab = self.driver.current_window_handle  # save default page
        touch_with_us.move_to_about_nepse_alpha()
        time.sleep(1)
        touch_with_us.click_facebook_button()
        time.sleep(1)
        fb_tab = self.driver.window_handles[1]  # save fb tab
        self.driver.switch_to.window(fb_tab)  # switch to fb tab
        time.sleep(2)
        touch_with_us.click_close_button_on_fb_dialog_box()
        time.sleep(2)
        assert self.driver.current_url == "https://www.facebook.com/nepsealpha"
        self.driver.close()  # close fb tab
        self.driver.switch_to.window(main_tab)  # switch to default page

    @pytest.mark.order(16)
    def test_verify_youtube_button_redirects_to_youtube_page(self):
        touch_with_us = GetInTouchWithUsSection(self.driver)
        touch_with_us.move_to_about_nepse_alpha()
        time.sleep(1)
        main_tab = self.driver.current_window_handle  # save default page
        touch_with_us.click_youtube_button()
        time.sleep(1)
        youtube_tab = self.driver.window_handles[1]  # save youtube tab
        self.driver.switch_to.window(youtube_tab)  # switch to youtube tab
        time.sleep(2)
        touch_with_us.check_youtube_element()
        self.driver.close()  # close fb tab
        self.driver.switch_to.window(main_tab)  # switch to default page
