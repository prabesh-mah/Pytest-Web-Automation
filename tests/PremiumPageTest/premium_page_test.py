from webpages.PremiumPage.PremiumPage import PremiumPage
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.medium_priority
class TestPremiumPage(BaseTest):

    @pytest.mark.order(23)
    def test_verify_khalti_button_redirects_to_khalti_page(self):
        premium_page = PremiumPage(self.driver)
        premium_page.click_premium()
        premium_page.scroll_using_js(650)
        premium_page.click_khalti_button()
        time.sleep(2)
        assert 'khalti' in premium_page.driver.current_url
        time.sleep(1)

    @pytest.mark.order(24)
    def test_verify_esewa_button_redirects_to_esewa_page(self):
        premium_page = PremiumPage(self.driver)
        premium_page.click_premium()
        premium_page.scroll_using_js(650)
        premium_page.click_esewa_button()
        time.sleep(2)
        assert 'esewa' in self.driver.current_url
        time.sleep(1)

    @pytest.mark.order(25)
    def test_verify_connectips_button_redirects_to_connectips_page(self):
        premium_page = PremiumPage(self.driver)
        premium_page.click_premium()
        premium_page.scroll_using_js(650)
        premium_page.click_connect_ips_button()
        time.sleep(2)
        assert 'connectips' in self.driver.current_url
        time.sleep(1)
