from webpages.HomePage.CompanyLogo import CompanyLogoSection
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestCompanyLogoVisibility(BaseTest):

    @pytest.mark.order(1)
    @pytest.mark.timeout(60)
    @pytest.mark.high_priority
    def test_is_company_logo_visible(self):
        logo = CompanyLogoSection(self.driver)
        logo.is_company_logo_visible()
