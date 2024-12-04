
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def add_transaction(driver):
    description, amount= "Test Income", "100"
    text_input = driver.find_element(By.ID, 'text')
    amount_input = driver.find_element(By.ID, 'amount')
    add_button = driver.find_element(By.CSS_SELECTOR, '.btn')
    
    text_input.send_keys(description)
    amount_input.send_keys(amount)
    add_button.click()
    time.sleep(2)  # Wait for the transaction to be added

def add_invalid_transaction(driver):
    add_button = driver.find_element(By.CSS_SELECTOR, '.btn')
    add_button.click()
    time.sleep(2)  # Wait for the notification to appear

def delete_transaction(driver):
    delete_button = driver.find_element(By.CSS_SELECTOR, '.delete-btn')
    delete_button.click()
    time.sleep(2)  # Wait for the transaction to be deleted

actions = [add_transaction, add_invalid_transaction, delete_transaction]

def interact(driver, dir):
    # Save the initial UI
    save_initial_screenshot(driver, dir)
    
    # Add a valid transaction
    add_transaction(driver, "Test Income", "100")
    driver.save_screenshot(f'{dir}/_images/after_add_transaction.png')
    
    # Add an invalid transaction
    add_invalid_transaction(driver)
    driver.save_screenshot(f'{dir}/_images/after_invalid_transaction.png')
    
    # Delete the transaction
    delete_transaction(driver)
    driver.save_screenshot(f'{dir}/_images/after_delete_transaction.png')
