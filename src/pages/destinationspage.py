from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pages.basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains



class DestinationsPage(BasePage):
    
    
    def __init__(self, driver):
        super().__init__(driver)


    def is_destination_page_loaded(self):
        return self.wait_for_element_visible((By.ID, "hero-section"))
    

    def right_button_visible(self):
        section = self.wait_for_element_visible((By.ID, "destination-fishing-seasons"))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", section) 
        actions = ActionChains(self.driver)
        actions.move_to_element(section).perform()
        right_button = (By.CSS_SELECTOR, "#destination-fishing-seasons .swiper-next-button")
        return self.wait_for_element_visible(right_button)



    def click_right_button(self):
        right_button = (By.CSS_SELECTOR, "#destination-fishing-seasons .swiper-next-button")
        self.wait_and_click(right_button)

    def is_october_visible(self):
        october_locator = (By.XPATH, "//span[contains(text(), 'October')]")
        return self.wait_for_element_visible(october_locator)