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

        # expected_company_name = "Nepse Alpha Pvt Ltd."
        # expected_symbol = "©"

        # company_name_matches = copyright.copyright_company_name_text(
        #     expected_company_name)
        # print(f"The copyright text matches the expected company name: {
        #     expected_company_name}")
        # assert company_name_matches, f"The copyright text does not match the expected company name: {
        #     expected_company_name}"

        # symbol_matches = copyright.copyright_symbol(expected_symbol)
        # print(f"The copyright symbol matches the expected symbol: {
        #     expected_symbol}")
        # assert symbol_matches, f"The copyright symbol does not match the expected symbol: {
        #     expected_symbol}"

        expected_name = '© Copyright Nepse Alpha Pvt Ltd.'

        copyright_text_matches = copyright.copyright_verfication(
            expected_name)
        if copyright_text_matches:
            print(f"The copyright text matches the expected company name: {
                expected_name}")
        else:
            assert False, f"The copyright text does not match the expected company name: {
                expected_name}"
