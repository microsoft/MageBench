
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_left_button(driver):
    left_button = driver.find_element(By.XPATH, "//button[contains(text(),'←')]")
    left_button.click()
    time.sleep(1)  # Wait for any animations or changes

def click_right_button(driver):
    right_button = driver.find_element(By.XPATH, "//button[contains(text(),'→')]")
    right_button.click()
    time.sleep(1)  # Wait for any animations or changes

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Click left button
    click_left_button(driver)
    # Save after clicking left button
    driver.save_screenshot(f'{dir}/_images/after_click_left.png') 
    # Click right button
    click_right_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_right.png') 
