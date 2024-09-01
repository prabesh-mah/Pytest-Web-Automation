from webpages.HomePage.CopyRight import CopyrightSection
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestCopyright(BaseTest):

    @pytest.mark.order(21)
    @pytest.mark.timeout(30)
    @pytest.mark.high_priority
    def test_verify_copyright_text_and_symbol(self):
        copyright = CopyrightSection(self.driver)

        expected_company_name = "Nepse Alpha Pvt Ltd."
        expected_symbol = "©"

        company_name_matches = copyright.copyright_company_name_text(
            expected_company_name)
        symbol_matches = copyright.copyright_symbol(expected_symbol)

        if company_name_matches and symbol_matches:
            print(f"The copyright text matches the:\n{expected_company_name}")
            print(f"The copyright symbol matches the:\n{expected_symbol}")
        else:
            if not company_name_matches:
                print(f"The copyright text does not match the:\n{
                      expected_company_name}")
            if not symbol_matches:
                print(f"The copyright symbol does not match the:\n{
                      expected_symbol}")
