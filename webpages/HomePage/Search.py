from webpages.BasePage import BasePage
from webpages.BaseLocators import SearchBoxLocator, HomepageLocator
from selenium.webdriver.common.by import By


class SearchBoxLocators:
    # Invalid Search
    not_found_404 = (By.XPATH, "//h1[normalize-space()='404']")

    # Search Term to Print Length of Child Elements
    search_asian = (
        By.XPATH, "//div[@class='autocomplete-items']")

    # Autosuggestion Items
    autosuggestion_item_ahl = (By.XPATH, "//div[text()='(AHL) Asia']")
    autosuggestion_item_nica = (
        By.XPATH, "//div[contains(@class, '-list') and contains(normalize-space(),'(NICA) NIC') and contains(normalize-space(),'Bank Ltd.')]")
    autosuggestion_item_nepse = (
        By.XPATH, "//div[contains(@class,'-list')]/b[text()='NEPSE']")
    autosuggestion_item_lbbl_debenture_2089 = (
        By.XPATH, "//div[contains(@class, '-list') and contains(normalize-space(),'LBBL Debenture 2089')]")

    # Redirection Pages
    ahl_page_element = (
        By.XPATH, "//h4[normalize-space()='Asian Hydropower Limited']")


class SearchBox(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_search_box_element(self):
        return self.check_element(SearchBoxLocator.search_box)

    def enter_search_term(self, keyword):
        return self.type(SearchBoxLocator.search_box, keyword)

    def click_search_button(self):
        self.click(SearchBoxLocator.search_button)

    def check_404_error_in_new_page(self):
        return self.check_element(SearchBoxLocators.not_found_404)

    def check_hompage_company_logo_element(self):
        return self.check_element(HomepageLocator.company_logo)

    def len_of_direct_child_element(self):
        return super().len_of_direct_child_element(SearchBoxLocators.search_asian)

    def hover_and_click_AHL(self):
        return super().move_to_element_and_click(SearchBoxLocators.autosuggestion_item_ahl)

    def hover_and_click_NICA(self):
        return super().move_to_element_and_click(SearchBoxLocators.autosuggestion_item_nica)

    def hover_and_click_NEPSE(self):
        return super().move_to_element_and_click(SearchBoxLocators.autosuggestion_item_nepse)

    def hover_and_click_LBBD89(self):
        return super().move_to_element_and_click(SearchBoxLocators.autosuggestion_item_lbbl_debenture_2089)
