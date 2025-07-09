from src.pages.sitemap import SitemapPage
from src.config import BASE_URL
from src.pages.homepage import HomePage
from src.pages.destinationspage import DestinationsPage 
    


def test_site_navigation(driver):
    driver.set_window_size(1440,900)
    driver.get(BASE_URL)
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    
    sitemap_page = SitemapPage(driver)

    assert sitemap_page.is_sitemap_loaded(), "Sitemap page did not load properly"

    # Insert your test here

    sitemap_page.click_on_homePage()
    home_page = HomePage(driver)
    assert home_page.is_homepage_loaded(), "Home page did not load properly"

    home_page.click_on_amazing_destination()
    assert "destinations/location" in driver.current_url, f"Expected URL to contain 'destinations/location', but got {driver.current_url}"
    destinations_page = DestinationsPage(driver)
    assert destinations_page.is_destination_page_loaded(),  "Destination page did not load properly"
  
    assert destinations_page.right_button_visible(), "Right button is not visible on the destination page"
  
    destinations_page.click_right_button()
    assert destinations_page.is_october_visible(), "October is not visible after clicking the right button"








    



