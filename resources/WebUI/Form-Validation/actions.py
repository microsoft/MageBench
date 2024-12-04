
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def fill_username(driver):
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('')
    time.sleep(1)

def fill_email(driver):
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys('')
    time.sleep(1)

def fill_password1(driver):
    password1_input = driver.find_element(By.ID, 'password1')
    password1_input.send_keys('')
    time.sleep(1)

def fill_password2(driver):
    password2_input = driver.find_element(By.ID, 'password2')
    password2_input.send_keys('')
    time.sleep(1)

def submit_form(driver):
    submit_button = driver.find_element(By.CLASS_NAME, 'submit')
    submit_button.click()
    time.sleep(2)

actions = [submit_form]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Fill username
    fill_username(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_username.png')
    
    # Fill email
    fill_email(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_email.png')
    
    # Fill password1
    fill_password1(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_password1.png')
    
    # Fill password2
    fill_password2(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_password2.png')
    
    # Submit form
    submit_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit.png')
