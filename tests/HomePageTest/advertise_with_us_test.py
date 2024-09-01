from webpages.HomePage.AdvertiseWithUs import AdvertiseWithUsSection
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.high_priority
class TestFooterLinks(BaseTest):

    @pytest.mark.order(17)
    @pytest.mark.timeout(60)
    def test_verify_address_and_contact_on_homepage(self):
        advertise_with_us = AdvertiseWithUsSection(self.driver)
        main_tab = self.driver.current_window_handle  # save default page
        advertise_with_us.click_adverise_with_us_element()
        advertise_tab = self.driver.window_handles[1]  # save advertise tab
        self.driver.switch_to.window(advertise_tab)  # switch to advertise tab
        time.sleep(2)
        assert self.driver.current_url == "https://www.nepsealpha.com/advertise-with-us"
        advertise_with_us.is_contact_visible_and_correct()
        advertise_with_us.is_email_address_visible_and_correct()
        self.driver.close()
        self.driver.switch_to.window(main_tab)  # switch to default page
