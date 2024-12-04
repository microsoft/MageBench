
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_copy_text(driver):
    copy_button = driver.find_element(By.CLASS_NAME, 'copyBtn')
    copy_button.click()
    time.sleep(0.1)  # Short sleep to see the "Content Copied" message

def click_move_text(driver):
    move_button = driver.find_element(By.CLASS_NAME, 'moverBtn')
    move_button.click()
    time.sleep(0.1)  # Sleep to ensure the text is moved

actions = [click_copy_text, click_move_text]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the copy button
    click_copy_text(driver)
    driver.save_screenshot(f'{dir}/_images/after_copy.png')
    
    # Click the move button
    click_move_text(driver)
    driver.save_screenshot(f'{dir}/_images/after_move.png')
