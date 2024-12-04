
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def set_password_length(driver):
    length_input = driver.find_element(By.ID, 'length')
    length_input.clear()
    length_input.send_keys('12')
    time.sleep(1)

def toggle_uppercase(driver):
    uppercase_checkbox = driver.find_element(By.ID, 'uppercase')
    if uppercase_checkbox.is_selected():
        uppercase_checkbox.click()
    time.sleep(1)

def toggle_numbers(driver):
    numbers_checkbox = driver.find_element(By.ID, 'numbers')
    if numbers_checkbox.is_selected():
        numbers_checkbox.click()
    time.sleep(1)

def generate_password(driver):
    generate_button = driver.find_element(By.ID, 'generate')
    generate_button.click()
    time.sleep(2)

actions = [set_password_length, toggle_uppercase, toggle_numbers, generate_password]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Set password length
    set_password_length(driver)
    driver.save_screenshot(f'{dir}/_images/after_set_length.png')
    
    # Toggle uppercase letters
    toggle_uppercase(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle_uppercase.png')
    
    # Toggle numbers
    toggle_numbers(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle_numbers.png')
    
    # Generate password
    generate_password(driver)
    driver.save_screenshot(f'{dir}/_images/after_generate_password.png')
