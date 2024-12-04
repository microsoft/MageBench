
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def fill_name(driver):
    name_input = driver.find_element(By.ID, 'name')
    name_input.send_keys('John Doe')
    time.sleep(1)

def fill_email(driver):
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys('john.doe@example.com')
    time.sleep(1)

def fill_password(driver):
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('password123')
    time.sleep(1)

def submit_form(driver):
    submit_button = driver.find_element(By.ID, 'submitBtn')
    submit_button.click()
    time.sleep(2)

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Fill in the name
    fill_name(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_name.png')
    
    # Fill in the email
    fill_email(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_email.png')
    
    # Fill in the password
    fill_password(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_password.png')
    
    # Submit the form
    submit_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit.png')

actions = [fill_name, fill_email, fill_password, submit_form]
