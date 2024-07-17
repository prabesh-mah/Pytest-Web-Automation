from webpages.HomePage.MoveToTop import MoveToTop
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.timeout(20)
@pytest.mark.low_priority
class TestMoveToTopButton(BaseTest):

    @pytest.mark.order(20)
    def test_check_move_to_top_button_redirects_to_top_of_page(self):
        move_to_top = MoveToTop(self.driver)
        move_to_top.navigate_to_end_of_page()
        time.sleep(1)
        move_to_top.click_movetotop_button()
        time.sleep(2)
        header_news_carousel_element = move_to_top.header_news_carousel_element()

        if header_news_carousel_element.is_displayed():
            print("Successfully moved to top")
        else:
            print("Failed to move to top")

        time.sleep(2)
