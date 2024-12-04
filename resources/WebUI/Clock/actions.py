
from selenium.webdriver.common.by import By
import time

def capture_initial_state(driver):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def wait_for_clock_update(driver):
    time.sleep(5)  # Wait for 5 seconds to capture the clock hands movement

actions = []

def interact(driver, dir):
    # Save the initial state of the clock
    capture_initial_state(driver)
    # Wait for the clock to update
    wait_for_clock_update(driver)
    # Save the state after waiting
    driver.save_screenshot(f'{dir}/_images/after_wait.png')
