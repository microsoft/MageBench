
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def toggle_theme(driver):
    theme_toggler = driver.find_element(By.ID, 'theme-toggler')
    theme_toggler.click()
    time.sleep(2)

def perform_search(driver):
    search_input = driver.find_element(By.ID, 'search-input')
    search_input.send_keys('Python programming')
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    search_button.click()
    time.sleep(2)  # Wait for search results to load

def handle_empty_search(driver):
    search_input = driver.find_element(By.ID, 'search-input')
    search_input.clear()
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    search_button.click()
    time.sleep(2)

def handle_no_results(driver):
    search_input = driver.find_element(By.ID, 'search-input')
    search_input.clear()
    search_input.send_keys('asdkjfhaksjdfh')
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    search_button.click()
    time.sleep(2)  # Wait for search results to load

def handle_search_error(driver):
    # Simulate an error by disconnecting the network or using an invalid endpoint
    # This is a placeholder function as simulating network errors is complex
    pass

actions = [toggle_theme, perform_search, handle_empty_search, handle_no_results]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Toggle theme
    toggle_theme(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle_theme.png')
    
    # Perform a search
    perform_search(driver)
    driver.save_screenshot(f'{dir}/_images/after_search.png')
    
    # Handle empty search
    handle_empty_search(driver)
    driver.save_screenshot(f'{dir}/_images/after_empty_search.png')
    
    # Handle no results found
    handle_no_results(driver)
    driver.save_screenshot(f'{dir}/_images/after_no_results.png')
