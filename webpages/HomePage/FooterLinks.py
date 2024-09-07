from webpages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import requests


class FooterLinksLocator:
    footer_links = (By.XPATH, "//div[@class='footer_links']/a")


class FooterLinkSection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_all_footer_links(self):
        footer_links = self.check_elements(FooterLinksLocator.footer_links)

        for link in footer_links:
            url = link.get_attribute("href")  # get href from HTML Tag

            try:
                # Send HTTP HEAD request to all URLs
                response = requests.head(url, timeout=10)
                if response.status_code >= 400:  # Check for broken links
                    print(f"Broken link: {
                          url} - Status code: {response.status_code}")
                else:
                    print(
                        f"Link {url} is working fine - Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error accessing {url}: {e}")
