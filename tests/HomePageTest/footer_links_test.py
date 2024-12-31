from webpages.HomePage.FooterLinks import FooterLinkSection
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestToggleTheme:

    @pytest.mark.order(32)
    @pytest.mark.timeout(60)
    @pytest.mark.xfail(reason="Single IP hit website multiple times so it might require proxy to pass the test")
    @pytest.mark.high_priority
    def test_all_footer_links_verification(self):
        footer_links = FooterLinkSection(self.driver)
        footer_links.validate_footer_links()
 