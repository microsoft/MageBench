
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def toggle_sidebar(driver):
    menu_button = driver.find_element(By.ID, 'menu')
    menu_button.click()
    time.sleep(1)  # wait for the animation to complete

def fill_registration_form(driver):
    name_input = driver.find_element(By.XPATH, '//input[@type="text"]')
    email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
    password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
    confirm_password_input = driver.find_element(By.XPATH, '(//input[@type="password"])[2]')
    
    name_input.send_keys("John Doe")
    email_input.send_keys("john.doe@example.com")
    password_input.send_keys("password123")
    confirm_password_input.send_keys("password123")
    time.sleep(1)  # wait for the inputs to be filled

actions = [toggle_sidebar]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Toggle sidebar
    toggle_sidebar(driver)
    driver.save_screenshot(f'{dir}/_images/sidebar_open.png')
    
    # Fill the registration form
    fill_registration_form(driver)
    driver.save_screenshot(f'{dir}/_images/form_filled.png')
