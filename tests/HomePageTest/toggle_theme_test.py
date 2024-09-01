from webpages.HomePage.ToggleTheme import ThemeSection, ThemeLocators
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
class TestToggleTheme(BaseTest):

    @pytest.mark.order(2)
    @pytest.mark.timeout(60)
    @pytest.mark.high_priority
    def test_toggle_theme_between_light_and_dark_mode(self):
        toggle_theme = ThemeSection(self.driver)

        def toggle_theme_and_verify(expected_theme):
            toggle_theme.click_more_tools()
            toggle_theme.click_toggle_theme()
            body_classes = toggle_theme.get_attribute(
                ThemeLocators.body, 'class')
            assert expected_theme in body_classes, f"Expected theme '{
                expected_theme}' not found."

        toggle_theme_and_verify('dark-nepse')
        self.driver.refresh()
        toggle_theme_and_verify('light-nepse')

        time.sleep(2)
