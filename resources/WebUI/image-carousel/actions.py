
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_next(driver):
    next_button = driver.find_element(By.ID, 'right')
    next_button.click()
    time.sleep(1)  # wait for the transition to complete

def click_prev(driver):
    prev_button = driver.find_element(By.ID, 'left')
    prev_button.click()
    time.sleep(1)  # wait for the transition to complete

actions = [click_next, click_prev]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    
    # Click next button
    click_next(driver)
    driver.save_screenshot(f'{dir}/_images/after_next.png') 
    
    # Click prev button
    click_prev(driver)
    driver.save_screenshot(f'{dir}/_images/after_prev.png') 
