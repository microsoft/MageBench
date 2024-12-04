
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def enter_search_term(driver):
    search_input = driver.find_element(By.ID, 'search-input')
    search_input.send_keys('nature')
    time.sleep(1)

def click_search_button(driver):
    search_button = driver.find_element(By.ID, 'search-button')
    search_button.click()
    time.sleep(2)  # Wait for images to load

def click_show_more_button(driver):
    show_more_button = driver.find_element(By.ID, 'show-more-button')
    show_more_button.click()
    time.sleep(2)  # Wait for more images to load

actions = [enter_search_term, click_search_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Enter search term
    enter_search_term(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_search_term.png')
    
    # Click search button
    click_search_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_search_button.png')
    
    # Click show more button
    click_show_more_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_show_more_button.png')
