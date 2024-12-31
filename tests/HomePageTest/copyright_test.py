from webpages.HomePage.CopyRight import CopyrightSection
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestCopyrightLink:

    @pytest.mark.order(21)
    @pytest.mark.timeout(30)
    @pytest.mark.high_priority
    def test_verify_copyright_text_and_symbol(self):
        copyright = CopyrightSection(self.driver)

        expected_name = '© Copyright Nepse Alpha Pvt Ltd.'

        copyright_text_matches = copyright.copyright_verfication(
            expected_name)
        if copyright_text_matches:
            print(f"The copyright text matches the expected company name: {
                expected_name}")
        else:
            assert False, f"The copyright text does not match the expected company name: {
                expected_name}"
