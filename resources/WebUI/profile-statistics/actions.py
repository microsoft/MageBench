
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def wait_for_counters_to_finish(driver):
    time.sleep(2)  # Wait for the counters to finish incrementing

actions = []

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    # Wait for counters to finish
    wait_for_counters_to_finish(driver)
    # Save after counters finish
    driver.save_screenshot(f'{dir}/_images/after_counters.png')
