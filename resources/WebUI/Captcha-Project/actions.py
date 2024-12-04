
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def reload_captcha(driver):
    reload_button = driver.find_element(By.CLASS_NAME, 'reload-btn')
    reload_button.click()
    time.sleep(1)  # wait for the CAPTCHA to reload

def enter_captcha(driver):
    captcha_text = driver.find_element(By.CLASS_NAME, 'captcha').text
    input_field = driver.find_element(By.TAG_NAME, 'input')
    input_field.send_keys(captcha_text)
    time.sleep(1)  # wait for the input to be processed

def check_captcha(driver):
    check_button = driver.find_element(By.CLASS_NAME, 'check-btn')
    check_button.click()
    time.sleep(1)  # wait for the status to be displayed

actions = [reload_captcha, enter_captcha, check_captcha]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Reload the CAPTCHA
    reload_captcha(driver)
    driver.save_screenshot(f'{dir}/_images/after_reload.png')
    
    # Enter the CAPTCHA
    enter_captcha(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter.png')
    
    # Check the CAPTCHA
    check_captcha(driver)
    driver.save_screenshot(f'{dir}/_images/after_check.png')
