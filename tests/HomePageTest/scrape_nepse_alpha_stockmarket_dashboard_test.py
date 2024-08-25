from webpages.HomePage.NepseAlphaStockMarketDashboard import ScrapeNepseStockMarketDashboard
from tests.base_test import BaseTest
import pytest


class TestNepseDashboardScrapping(BaseTest):

    def test_scrape_nepse_alpha_stockmarket_dashboard(self):
        nepse_dashboard = ScrapeNepseStockMarketDashboard(self.driver)
        nepse_dashboard.scrape_current_table()
