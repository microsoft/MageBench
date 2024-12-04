
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_down_button(driver):
    down_button = driver.find_element(By.CLASS_NAME, 'down-button')
    down_button.click()
    time.sleep(2)  # wait for the slide transition

def click_up_button(driver):
    up_button = driver.find_element(By.CLASS_NAME, 'up-button')
    up_button.click()
    time.sleep(2)  # wait for the slide transition

actions = [click_down_button, click_up_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    
    # Click down button
    click_down_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_down.png') 
    
    # Click up button
    click_up_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_up.png') 
