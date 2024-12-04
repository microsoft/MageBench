
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_sign_up(driver):
    sign_up_button = driver.find_element(By.ID, 'signUp')
    sign_up_button.click()
    time.sleep(2)  # Wait for the animation to complete

def click_sign_in(driver):
    sign_in_button = driver.find_element(By.ID, 'signIn')
    sign_in_button.click()
    time.sleep(2)  # Wait for the animation to complete

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on Sign Up button
    click_sign_up(driver)
    driver.save_screenshot(f'{dir}/_images/after_sign_up.png')
    
    # Click on Sign In button
    click_sign_in(driver)
    driver.save_screenshot(f'{dir}/_images/after_sign_in.png')

actions = [click_sign_up, click_sign_in]
