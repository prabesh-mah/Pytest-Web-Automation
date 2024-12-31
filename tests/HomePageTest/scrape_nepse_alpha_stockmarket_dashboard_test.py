from webpages.HomePage.NepseAlphaStockMarketDashboard import ScrapeNepseStockMarketDashboard
import pytest


class TestNepseDashboardScrapping:

    @pytest.mark.order(31)
    @pytest.mark.timeout(30)
    @pytest.mark.low_priority
    def test_scrape_nepse_alpha_stockmarket_dashboard(self):
        nepse_dashboard = ScrapeNepseStockMarketDashboard(self.driver)
        nepse_dashboard.scrape_current_table()
