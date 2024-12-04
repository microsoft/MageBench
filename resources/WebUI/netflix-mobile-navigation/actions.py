
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def open_navigation_menu(driver):
    open_button = driver.find_element(By.CLASS_NAME, 'open-btn')
    open_button.click()
    time.sleep(2)  # Wait for the animation to complete

def close_navigation_menu(driver):
    close_button = driver.find_element(By.CLASS_NAME, 'close-btn')
    close_button.click()
    time.sleep(2)  # Wait for the animation to complete

actions = [open_navigation_menu, close_navigation_menu]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    
    # Open the navigation menu
    open_navigation_menu(driver)
    driver.save_screenshot(f'{dir}/_images/after_open.png') 
    
    # Close the navigation menu
    close_navigation_menu(driver)
    driver.save_screenshot(f'{dir}/_images/after_close.png') 
