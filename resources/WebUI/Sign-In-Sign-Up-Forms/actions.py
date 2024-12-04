
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_sign_up(driver):
    sign_up_button = driver.find_element(By.CLASS_NAME, 'signup-btn')
    sign_up_button.click()
    time.sleep(2)  # wait for the animation to complete

def click_sign_in(driver):
    sign_in_button = driver.find_element(By.CLASS_NAME, 'signin-btn')
    sign_in_button.click()
    time.sleep(2)  # wait for the animation to complete

def fill_sign_up_form(driver):
    driver.find_element(By.ID, 'username').send_keys('TestUser')
    driver.find_element(By.ID, 'email').send_keys('testuser@example.com')
    driver.find_element(By.ID, 'password').send_keys('password123')
    driver.find_element(By.ID, 'password2').send_keys('password123')
    time.sleep(1)  # wait for inputs to be filled

def submit_form(driver):
    submit_button = driver.find_element(By.CLASS_NAME, 'form-btn')
    submit_button.click()
    time.sleep(2)  # wait for form submission

actions = [click_sign_up, fill_sign_up_form, submit_form]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click Sign Up button
    click_sign_up(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_sign_up.png')
    
    # Fill Sign Up form
    fill_sign_up_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_sign_up_form.png')
    
    # Submit Sign Up form
    submit_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit_sign_up_form.png')
    
    # Click Sign In button
    click_sign_in(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_sign_in.png')
