from webpages.HomePage.MoveToTop import MoveToTop
import pytest
import time


@pytest.mark.regression
class TestMoveToTopButton:

    @pytest.mark.order(20)
    @pytest.mark.medium_priority
    @pytest.mark.skip(reason="The button has been removed")
    def test_check_move_to_top_button_redirects_to_top_of_page(self):
        move_to_top = MoveToTop(self.driver)
        move_to_top.navigate_to_end_of_page()
        time.sleep(1)
        move_to_top.click_movetotop_button()
        time.sleep(2)
