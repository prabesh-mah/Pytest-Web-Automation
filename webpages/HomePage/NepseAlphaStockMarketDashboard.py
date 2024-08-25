from webpages.BasePage import BasePage
from selenium.webdriver.common.by import By
import pandas as pd


class NepseStockMarketDashboardLocator:
    index = (
        By.XPATH, "(//tbody)[2]/tr/td[@class='first-col title fixed-left-header']")
    current = (By.XPATH, "(//tbody)[2]/tr/td[2]")
    turnover = (By.XPATH, "(//tbody)[2]/tr/td[3]")
    pe = (By.XPATH, "(//tbody)[2]/tr/td[5]")
    pb = (By.XPATH, "(//tbody)[2]/tr/td[6]")
    div_yield = (By.XPATH, "(//tbody)[2]/tr/td[7]")
    rsi = (By.XPATH, "(//tbody)[2]/tr/td[9]")
    alpha = (By.XPATH, "(//tbody)[2]/tr/td[11]")
    beta = (By.XPATH, "(//tbody)[2]/tr/td[12]")


class ScrapeNepseStockMarketDashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_total_rows(self):
        # Get all rows from the table
        return len(self.driver.find_elements(*NepseStockMarketDashboardLocator.index))

    def scrape_current_table(self):
        stock_market_dashboard_results = []  # empty list
        total_rows = self.get_total_rows()  # get total number of rows

        for i in range(total_rows):
            # Fetch data for each row
            row_data = {
                'Index': self.get_element_text_with_index(NepseStockMarketDashboardLocator.index, i),
                'Current': self.get_element_text_with_index(NepseStockMarketDashboardLocator.current, i),
                'Turnover': self.get_element_text_with_index(NepseStockMarketDashboardLocator.turnover, i),
                'PE': self.get_element_text_with_index(NepseStockMarketDashboardLocator.pe, i),
                'PB': self.get_element_text_with_index(NepseStockMarketDashboardLocator.pb, i),
                'Div_Yield': self.get_element_text_with_index(NepseStockMarketDashboardLocator.div_yield, i),
                'Rsi': self.get_element_text_with_index(NepseStockMarketDashboardLocator.rsi, i),
                'Alpha': self.get_element_text_with_index(NepseStockMarketDashboardLocator.alpha, i),
                'Beta': self.get_element_text_with_index(NepseStockMarketDashboardLocator.beta, i)
            }
            stock_market_dashboard_results.append(
                row_data)  # append result to empty list from start

        # Create DataFrame and save to Excel once
        file = pd.DataFrame(stock_market_dashboard_results)
        file.to_excel(
            'tests/data/Nepse Alpha Stock Market Dashboard.xlsx', index=False)
