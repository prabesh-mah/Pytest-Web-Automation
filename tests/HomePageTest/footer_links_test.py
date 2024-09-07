from webpages.HomePage.FooterLinks import FooterLinkSection
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestToggleTheme(BaseTest):

    @pytest.mark.order(32)
    @pytest.mark.timeout(60)
    @pytest.mark.xfail(reason="Single IP hit website multiple times so it might require proxy to pass the test")
    @pytest.mark.high_priority
    def test_all_footer_links_verification(self):
        footer_links = FooterLinkSection(self.driver)
        footer_links.verify_all_footer_links()
