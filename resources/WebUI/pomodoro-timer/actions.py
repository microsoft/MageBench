
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_start(driver):
    start_button = driver.find_element(By.ID, 'start')
    start_button.click()
    time.sleep(2)  # Wait for a few seconds to show the timer running

def click_stop(driver):
    stop_button = driver.find_element(By.ID, 'stop')
    stop_button.click()
    time.sleep(1)  # Short wait to ensure the timer stops

def click_reset(driver):
    reset_button = driver.find_element(By.ID, 'reset')
    reset_button.click()
    time.sleep(1)  # Short wait to ensure the timer resets

actions = [click_start, click_stop, click_reset]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Click start
    click_start(driver)
    # Save after starting the timer
    driver.save_screenshot(f'{dir}/_images/after_start.png') 
    # Click stop
    click_stop(driver)
    # Save after stopping the timer
    driver.save_screenshot(f'{dir}/_images/after_stop.png') 
    # Click reset
    click_reset(driver)
    # Save after resetting the timer
    driver.save_screenshot(f'{dir}/_images/after_reset.png') 
