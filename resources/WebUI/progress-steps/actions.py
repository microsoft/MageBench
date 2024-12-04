
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_next(driver):
    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(1)  # wait for the progress bar to update

def click_prev(driver):
    prev_button = driver.find_element(By.ID, 'prev')
    prev_button.click()
    time.sleep(1)  # wait for the progress bar to update

actions = [click_next, click_prev]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click next button and save screenshot
    click_next(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_next_1.png')
    
    # Click next button again and save screenshot
    click_next(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_next_2.png')
    
    # Click prev button and save screenshot
    click_prev(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_prev_1.png')
    
    # Click prev button again and save screenshot
    click_prev(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_prev_2.png')
