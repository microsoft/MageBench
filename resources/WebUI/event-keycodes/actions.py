
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def press_keyA(driver):
    actions = ActionChains(driver)
    actions.send_keys('A').perform()
    time.sleep(2)  # Wait for the key press event to be processed

def press_keyS(driver):
    actions = ActionChains(driver)
    actions.send_keys(' ').perform()
    time.sleep(2)  # Wait for the key press event to be processed

actions = [press_keyA, press_keyS]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Press a key (e.g., 'A')
    press_keyA(driver)
    driver.save_screenshot(f'{dir}/_images/after_key_A.png')
    
    # Press another key (e.g., 'Space')
    press_keyS(driver)
    driver.save_screenshot(f'{dir}/_images/after_key_space.png')
