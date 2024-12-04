
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def search_word(driver):
    input_element = driver.find_element(By.ID, 'input')
    input_element.send_keys('example')
    input_element.send_keys(Keys.ENTER)
    time.sleep(2)  # Wait for the API response and UI update

def save_after_search_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/after_search.png')

actions = [search_word]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Search for a word
    search_word(driver)
    
    # Save after search
    save_after_search_screenshot(driver, dir)
