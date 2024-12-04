
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_toggle_button(driver):
    toggle_button = driver.find_element(By.ID, 'toggle')
    toggle_button.click()
    time.sleep(2)  # Wait for the animation to complete

actions = [click_toggle_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the toggle button to expand the navigation menu
    click_toggle_button(driver)
    
    # Save the screenshot after clicking the toggle button
    driver.save_screenshot(f'{dir}/_images/after_toggle.png')
