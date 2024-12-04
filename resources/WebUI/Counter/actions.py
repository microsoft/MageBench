
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_increment_button(driver):
    increment_button = driver.find_element(By.CLASS_NAME, 'increment-btn')
    increment_button.click()
    time.sleep(1)  # Wait for the count to update

def click_save_button(driver):
    save_button = driver.find_element(By.CLASS_NAME, 'save-btn')
    save_button.click()
    time.sleep(1)  # Wait for the save action to complete

actions = [click_increment_button, click_save_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click increment button
    click_increment_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_increment.png')
    
    # Click save button
    click_save_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_save.png')
