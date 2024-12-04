
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def fill_username(driver):
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('testuser')
    time.sleep(1)

def fill_email(driver):
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys('test@example.com')
    time.sleep(1)

def fill_password(driver):
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('password123')
    time.sleep(1)

def fill_password2(driver):
    password2_input = driver.find_element(By.ID, 'password2')
    password2_input.send_keys('password123')
    time.sleep(1)

def submit_form(driver):
    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()
    time.sleep(2)

actions = [fill_username, fill_email, fill_password, fill_password2, submit_form]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Fill username
    fill_username(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_username.png')
    
    # Fill email
    fill_email(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_email.png')
    
    # Fill password
    fill_password(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_password.png')
    
    # Fill password confirmation
    fill_password2(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_password2.png')
    
    # Submit form
    submit_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit.png')
