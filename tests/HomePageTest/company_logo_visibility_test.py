from webpages.HomePage.CompanyLogo import CompanyLogoSection
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.high_priority
class TestCompanyLogoVisibility(BaseTest):

    @pytest.mark.order(1)
    @pytest.mark.high_priority
    @pytest.mark.timeout(60)
    def test_is_company_logo_visible(self):
        logo = CompanyLogoSection(self.driver)
        logo.is_company_logo_visible()
