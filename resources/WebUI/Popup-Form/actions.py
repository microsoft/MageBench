
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_sign_up(driver):
    sign_up_button = driver.find_element(By.ID, 'open')
    sign_up_button.click()
    time.sleep(2)  # Wait for the modal to appear

def fill_form(driver):
    name_input = driver.find_element(By.ID, 'name')
    email_input = driver.find_element(By.ID, 'email')
    password_input = driver.find_element(By.ID, 'password')
    confirm_password_input = driver.find_element(By.ID, 'password2')
    
    name_input.send_keys("John Doe")
    email_input.send_keys("john.doe@example.com")
    password_input.send_keys("password123")
    confirm_password_input.send_keys("password123")
    time.sleep(2)  # Wait to simulate user input

def close_modal(driver):
    close_button = driver.find_element(By.ID, 'close')
    close_button.click()
    time.sleep(2)  # Wait for the modal to close

actions = [click_sign_up, fill_form, close_modal]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the "Sign Up" button
    click_sign_up(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_sign_up.png')
    
    # Fill the form
    fill_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_fill_form.png')
    
    # Close the modal
    close_modal(driver)
    driver.save_screenshot(f'{dir}/_images/after_close_modal.png')
