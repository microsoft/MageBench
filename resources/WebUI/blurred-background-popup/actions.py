
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_join_button(driver):
    join_button = driver.find_element(By.CLASS_NAME, 'btn')
    join_button.click()
    time.sleep(1)  # Wait for the popup to appear

def close_popup(driver):
    close_icon = driver.find_element(By.CLASS_NAME, 'close-icon')
    close_icon.click()
    time.sleep(1)  # Wait for the popup to disappear

actions = [click_join_button, close_popup]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the join button to show the popup
    click_join_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_join.png')
    
    # Close the popup
    close_popup(driver)
    driver.save_screenshot(f'{dir}/_images/after_close_popup.png')
