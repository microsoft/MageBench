
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def click_switch_to_login(driver):
    switch_to_login_button = driver.find_element(By.ID, 'switch1')
    switch_to_login_button.click()
    time.sleep(1)  # Wait for the animation to complete

def click_switch_to_register(driver):
    switch_to_register_button = driver.find_element(By.ID, 'switch2')
    switch_to_register_button.click()
    time.sleep(1)  # Wait for the animation to complete

def fill_login_form(driver):
    name_input = driver.find_element(By.CSS_SELECTOR, '.login input[placeholder="Name"]')
    email_input = driver.find_element(By.CSS_SELECTOR, '.login input[placeholder="Email"]')
    password_input = driver.find_element(By.CSS_SELECTOR, '.login input[placeholder="Password"]')
    
    name_input.send_keys("testuser")
    email_input.send_keys("testuser@example.com")
    password_input.send_keys("password123")
    time.sleep(1)  # Wait for the inputs to be filled

def fill_register_form(driver):
    name_input = driver.find_element(By.CSS_SELECTOR, '.register input[placeholder="Name"]')
    email_input = driver.find_element(By.CSS_SELECTOR, '.register input[placeholder="Email"]')
    password_input = driver.find_element(By.CSS_SELECTOR, '.register input[placeholder="Password"]')
    
    name_input.send_keys("newuser")
    email_input.send_keys("newuser@example.com")
    password_input.send_keys("newpassword123")
    time.sleep(1)  # Wait for the inputs to be filled

actions = [click_switch_to_login]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Click to switch to login form
    click_switch_to_login(driver)
    driver.save_screenshot(f'{dir}/_images/after_switch_to_login.png')
    
    # Fill the login form
    fill_login_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_login_form.png')
    
    # Click to switch to register form
    click_switch_to_register(driver)
    driver.save_screenshot(f'{dir}/_images/after_switch_to_register.png')
    
    # Fill the register form
    fill_register_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_register_form.png')
