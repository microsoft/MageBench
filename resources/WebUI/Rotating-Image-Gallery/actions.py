
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_next_button(driver):
    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(1)  # wait for the rotation animation to complete

def click_prev_button(driver):
    prev_button = driver.find_element(By.ID, 'prev')
    prev_button.click()
    time.sleep(1)  # wait for the rotation animation to complete

actions = [click_next_button, click_prev_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click next button
    click_next_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_next_click.png')
    
    # Click prev button
    click_prev_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_prev_click.png')
