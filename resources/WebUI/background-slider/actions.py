
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def click_right_arrow(driver):
    right_arrow = driver.find_element(By.ID, 'right')
    right_arrow.click()
    time.sleep(1)  # wait for the transition

def click_left_arrow(driver):
    left_arrow = driver.find_element(By.ID, 'left')
    left_arrow.click()
    time.sleep(1)  # wait for the transition

actions = [click_right_arrow, click_right_arrow, click_left_arrow]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Click right arrow twice
    click_right_arrow(driver)
    driver.save_screenshot(f'{dir}/_images/after_first_right_click.png')
    
    click_right_arrow(driver)
    driver.save_screenshot(f'{dir}/_images/after_second_right_click.png')
    
    # Click left arrow once
    click_left_arrow(driver)
    driver.save_screenshot(f'{dir}/_images/after_left_click.png')
