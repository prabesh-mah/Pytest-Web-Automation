from selenium.webdriver.common.by import By


class NavigationMenuLocator:
    home_button = (
        By.XPATH, "(//a[@class='navtitle' and contains(normalize-space(),'Home')])[1]")
    media_button = (
        By.XPATH, "(//a[@class='navtitle' and contains(normalize-space(),'Media')])[1]")
    trading_signals_button = (
        By.XPATH, "(//a[@class='navtitle' and contains(normalize-space(),'Trading Signals')])[1]")
    alpha_screen_button = (
        By.XPATH, "(//a[@class='navtitle' and contains(normalize-space(),'Alpha Screen')])[1]")
    investment_calendar_button = (
        By.XPATH, "(//a[@class='navtitle' and contains(normalize-space(),'Investment Calendar')])[1]")
    alpha_chart_button = (
        By.XPATH, "(//a[@class='navtitle' and contains(normalize-space(),'Alpha Charts')])[1]")
    investing_tools_button = (
        By.XPATH, "(//a[@class='navtitle' and contains(normalize-space(),'Investing Tools')])[1]")
    education_button = (
        By.XPATH, "(//a[@class='navtitle' and contains(normalize-space(),'Education')])[1]")
    premium_button = (
        By.XPATH, "(//a[@title='Sasto Share'][normalize-space()='Premium'])[1]")
    floorsheet_filter = (
        By.XPATH, "(//a[@title='Floorsheet Filter'])[1]")
    trader_floorsheet = (By.XPATH, "(//a[@title='Trader Floorsheet'])[1]")


class SearchBoxLocator:
    search_box = (By.XPATH, "//input[@id='__stock_symbol_search']")
    search_button = (By.XPATH, "//input[@id='searchBtn']")


class CopyRightLocator:
    copyright_symbol_and_text = (
        By.XPATH, "//div[@class='column column_2_3' and contains(normalize-space(),'© Copyright') and  contains(normalize-space(),'Nepse Alpha Pvt Ltd.') ]")


class HomepageLocator:
    about_nepse_alpha = (
        By.XPATH, "//h4[normalize-space()='About Nepse Alpha']")
    company_logo = (By.XPATH, "//img[@src='/images/logo.jpg']")
    nepse_alpha_fb_page = (
        By.XPATH, "//h4[normalize-space()='Nepse Alpha Facebook Page']")
    latest_anouncement_header = (
        By.XPATH, "//li[normalize-space()='Latest Announcement']")
