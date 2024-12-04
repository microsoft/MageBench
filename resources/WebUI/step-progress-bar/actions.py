
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_next(driver):
    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(1)  # Wait for the progress bar to update

def click_prev(driver):
    prev_button = driver.find_element(By.ID, 'prev')
    prev_button.click()
    time.sleep(1)  # Wait for the progress bar to update

actions = [click_next, click_prev]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click next to move to step 2
    click_next(driver)
    driver.save_screenshot(f'{dir}/_images/step_2.png')
    
    # Click next to move to step 3
    click_next(driver)
    driver.save_screenshot(f'{dir}/_images/step_3.png')
    
    # Click prev to move back to step 2
    click_prev(driver)
    driver.save_screenshot(f'{dir}/_images/step_2_back.png')
    
    # Click prev to move back to step 1
    click_prev(driver)
    driver.save_screenshot(f'{dir}/_images/step_1_back.png')
