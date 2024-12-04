
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def click_sign_up(driver):
    sign_up_btn = driver.find_element(By.CLASS_NAME, 'signup-btn')
    sign_up_btn.click()
    time.sleep(2)  # Wait for the animation to complete

def click_sign_in(driver):
    sign_in_btn = driver.find_element(By.CLASS_NAME, 'signin-btn')
    sign_in_btn.click()
    time.sleep(2)  # Wait for the animation to complete

actions = [click_sign_up, click_sign_in]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Click on Sign Up button
    click_sign_up(driver)
    driver.save_screenshot(f'{dir}/_images/after_sign_up.png')
    
    # Click on Sign In button
    click_sign_in(driver)
    driver.save_screenshot(f'{dir}/_images/after_sign_in.png')
