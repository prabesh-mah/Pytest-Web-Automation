from selenium.webdriver.common.keys import Keys
from webpages.HomePage.Search import SearchBox
from webpages.BasePage import BasePage
from tests.base_test import BaseTest
import pytest
import time


class TestSearchBox(BaseTest):

    @pytest.mark.order(3)
    @pytest.mark.timeout(30)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.high_priority
    def test_verify_visibility_of_search_box(self):
        search_box = SearchBox(self.driver)
        search_box.check_search_box_element()
        time.sleep(1)

    @pytest.mark.order(4)
    @pytest.mark.timeout(60)
    @pytest.mark.regression
    @pytest.mark.medium_priority
    def test_verify_search_with_extra_spaces_at_start_and_end(self):
        search_box = SearchBox(self.driver)
        to_search_1 = '          asia'
        to_search_2 = 'asia          '
        search_box.enter_search_term(to_search_1)
        search_box.hover_and_click_NICA()
        time.sleep(2)
        assert 'NICA' in self.driver.current_url
        self.driver.back()
        self.driver.refresh()
        search_box.enter_search_term(to_search_2)
        search_box.hover_and_click_NICA()
        time.sleep(2)
        assert 'NICA' in self.driver.current_url
        time.sleep(1)

    @pytest.mark.order(5)
    @pytest.mark.timeout(40)
    @pytest.mark.regression
    @pytest.mark.medium_priority
    def test_verify_search_with_different_datatype(self):
        search_box = SearchBox(self.driver)
        to_search = '11'
        search_box.enter_search_term(to_search)
        search_box.len_of_direct_child_element()
        search_box.hover_and_click_LBBD89()
        assert 'LBBLD89' in self.driver.current_url
        time.sleep(1)

    @pytest.mark.order(6)
    @pytest.mark.timeout(40)
    @pytest.mark.regression
    @pytest.mark.medium_priority
    def test_verify_search_with_invalid_keyword(self):
        search_box = SearchBox(self.driver)
        to_search = 'N$1#'
        search_box.enter_search_term(to_search)
        search_box.actions.send_keys(Keys.ENTER).perform()
        search_box.check_404_error_in_new_page()
        time.sleep(1)

    @pytest.mark.order(7)
    @pytest.mark.timeout(30)
    @pytest.mark.regression
    @pytest.mark.medium_priority
    def test_verify_search_with_empty_keyword(self):
        search_box = SearchBox(self.driver)
        to_search = ''
        search_box.enter_search_term(to_search)
        search_box.click_search_button()
        search_box.check_hompage_company_logo_element()
        time.sleep(1)

    @pytest.mark.order(8)
    @pytest.mark.timeout(30)
    @pytest.mark.regression
    @pytest.mark.high_priority
    def test_verify_search_with_autosuggestion_functionality(self):
        search_box = SearchBox(self.driver)
        to_search = 'asian'
        search_box.enter_search_term(to_search)
        search_box.len_of_direct_child_element()
        time.sleep(1)

    @pytest.mark.order(9)
    @pytest.mark.timeout(30)
    @pytest.mark.regression
    @pytest.mark.high_priority
    def test_verify_mouse_click_on_autosuggestion_item(self):
        search_box = SearchBox(self.driver)
        to_search = 'n'
        search_box.enter_search_term(to_search)
        search_box.hover_and_click_AHL()
        time.sleep(2)
        assert 'AHL' in self.driver.current_url
        time.sleep(1)

    @pytest.mark.order(10)
    @pytest.mark.timeout(30)
    @pytest.mark.regression
    @pytest.mark.medium_priority
    def test_verify_keyboard_navigation_on_autosuggestion_item(self):
        search_box = SearchBox(self.driver)
        to_search = 'n'
        search_box.enter_search_term(to_search)
        for i in range(4):
            search_box.actions.send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()
        time.sleep(2)
        assert 'ADBLB86' in self.driver.current_url

    @pytest.mark.order(11)
    @pytest.mark.timeout(60)
    @pytest.mark.regression
    @pytest.mark.medium_priority
    def test_verify_search_with_upper_lower_and_camel_case(self):
        search_box = SearchBox(self.driver)
        to_search_1 = 'asia'
        to_search_2 = 'ASIA'
        to_search_3 = 'aSiA'
        search_box.enter_search_term(to_search_1)
        search_box.hover_and_click_NICA()
        time.sleep(2)
        assert 'NICA' in self.driver.current_url
        self.driver.back()
        self.driver.refresh()
        search_box.enter_search_term(to_search_2)
        search_box.hover_and_click_NICA()
        time.sleep(2)
        assert 'NICA' in self.driver.current_url
        self.driver.back()
        self.driver.refresh()
        search_box.enter_search_term(to_search_3)
        search_box.hover_and_click_NICA()
        time.sleep(2)
        assert 'NICA' in self.driver.current_url
        time.sleep(1)

    @pytest.mark.order(12)
    @pytest.mark.timeout(30)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.high_priority
    def test_search_with_valid_keyword(self):
        search_box = SearchBox(self.driver)
        to_search = 'NEPSE'
        search_box.enter_search_term(to_search)
        search_box.actions.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        assert 'NEPSE' in self.driver.current_url
        time.sleep(1)
