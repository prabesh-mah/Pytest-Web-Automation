from webpages.HomePage.AboutNepseAlpha import AboutNepseAphaSection
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest


@pytest.mark.smoke
@pytest.mark.regression
class TestFooterLinks(BaseTest):

    @pytest.mark.order(13)
    @pytest.mark.timeout(30)
    @pytest.mark.high_priority
    def test_verify_address_and_contact_on_homepage(self):
        about_us = AboutNepseAphaSection(self.driver)
        about_us.move_to_element_using_js()
        about_us.is_address_visible_and_correct()
        about_us.is_mobile_num_visible_and_correct()
        about_us.is_landline_num_visible_and_correct()
