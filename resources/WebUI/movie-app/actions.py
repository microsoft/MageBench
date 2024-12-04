
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def wait_for_loading(driver):
    time.sleep(10)  # Wait for the movies to load

def search_movie(driver):
    search_input = driver.find_element(By.ID, 'search')
    search_input.send_keys('Spider man')
    search_input.submit()
    time.sleep(10)  # Wait for the search results to load

def hover_first_movie(driver):
    first_movie = driver.find_element(By.CSS_SELECTOR, '.movie')
    actions = ActionChains(driver)
    actions.move_to_element(first_movie).perform()
    time.sleep(2)  # Wait for the overview to be displayed

actions = [wait_for_loading, search_movie, hover_first_movie]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Wait for the initial movies to load
    wait_for_loading(driver)
    driver.save_screenshot(f'{dir}/_images/after_loading.png')
    
    # Search for a movie
    search_movie(driver)
    driver.save_screenshot(f'{dir}/_images/after_search.png')
    
    # Hover over the first movie
    hover_first_movie(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
