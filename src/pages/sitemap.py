from selenium.webdriver.common.by import By
from src.pages.basepage import BasePage

class SitemapPage(BasePage):
    PAGE_CONTENT = (By.ID, "main-content")

    def __init__(self, driver):
        super().__init__(driver)

    def is_sitemap_loaded(self):
        return self.wait_for_element_visible(self.PAGE_CONTENT) is not None

    def click_on_homePage(self):
        homePage_locator = ((By.LINK_TEXT, "Home"))
        self.wait_and_click(homePage_locator)