
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def enter_search_term(driver):
    search_input = driver.find_element(By.ID, 'search')
    search_input.send_keys('Michael Jackson')
    time.sleep(1)  # wait for input to be entered

def click_search_button(driver):
    search_button = driver.find_element(By.XPATH, '//form/button')
    search_button.click()
    time.sleep(2)  # wait for search results to load

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
