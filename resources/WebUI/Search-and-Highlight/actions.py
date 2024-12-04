
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def enter_search_text(driver):
    search_input = driver.find_element(By.ID, 'input')
    search_input.send_keys('Lorem')
    time.sleep(1)

def click_search_button(driver):
    search_button = driver.find_element(By.ID, 'searchBtn')
    search_button.click()
    time.sleep(2)

actions = [enter_search_text, click_search_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Enter search text
    enter_search_text(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_text.png')
    
    # Click search button
    click_search_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_search.png')
