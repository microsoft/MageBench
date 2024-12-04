
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def load_user_data(driver):
    # Wait for the user data to load
    time.sleep(2)  # Assuming it takes 5 seconds to load the data

def type_in_search_field(driver):
    search_field = driver.find_element(By.ID, 'filter')
    search_field.send_keys('L')
    time.sleep(2)  # Wait for the filtering to take effect

actions = [type_in_search_field]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Load user data
    load_user_data(driver)
    driver.save_screenshot(f'{dir}/_images/after_load.png')
    # Type in search field
    type_in_search_field(driver)
    driver.save_screenshot(f'{dir}/_images/after_search.png')
