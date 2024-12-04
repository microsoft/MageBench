
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def wait_for_content_load(driver):
    time.sleep(2)  # Wait for the content to load (2.5 seconds as per the script)

actions = []

def interact(driver, dir):
    # Save the original UI with placeholders
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Wait for the content to load and capture the state after loading
    wait_for_content_load(driver)
    driver.save_screenshot(f'{dir}/_images/after_content_load.png')
