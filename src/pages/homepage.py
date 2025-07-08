from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pages.basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains



class HomePage(BasePage):
    
    PAGE_CONTENT = (By.ID, "popular-destinations")
    def __init__(self, driver):
        super().__init__(driver)

    def is_homepage_loaded(self):
        return self.wait_for_element_visible(self.PAGE_CONTENT)
    

    def click_on_amazing_destination(self, index=1):
        amazing_dest =  (By.XPATH, "//h2[contains(text(), 'Amazing destinations')]")
        self.wait_for_element_visible(amazing_dest)
        locator = (By.CSS_SELECTOR, f'[data-testid="popular-destination-card-{index}"]')
        self.wait_and_click(locator)

    







        


