
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_state(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def wait_for_loading(driver, dir):
    time.sleep(2)  # Wait for the loading to complete and countdown to display
    driver.save_screenshot(f'{dir}/_images/after_loading.png')

actions = []

def interact(driver, dir):
    # Save the initial state
    save_initial_state(driver, dir)
    # Wait for loading to complete and save the state
    wait_for_loading(driver, dir)
