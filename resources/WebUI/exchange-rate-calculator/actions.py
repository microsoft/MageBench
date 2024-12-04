
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def select_currency_one(driver):
    currency_one = driver.find_element(By.ID, 'currency-one')
    for option in currency_one.find_elements(By.TAG_NAME, 'option'):
        if option.text == 'EUR':
            option.click()
            break
    time.sleep(2)

def input_amount_one(driver):
    amount_one = driver.find_element(By.ID, 'amount-one')
    amount_one.clear()
    amount_one.send_keys('100')
    time.sleep(2)

def select_currency_two(driver):
    currency_two = driver.find_element(By.ID, 'currency-two')
    for option in currency_two.find_elements(By.TAG_NAME, 'option'):
        if option.text == 'JPY':
            option.click()
            break
    time.sleep(2)

def swap_currencies(driver):
    swap_button = driver.find_element(By.ID, 'swap')
    swap_button.click()
    time.sleep(2)

def input_amount_two(driver):
    amount_two = driver.find_element(By.ID, 'amount-two')
    amount_two.clear()
    amount_two.send_keys('200')
    time.sleep(2)

actions = [select_currency_one, input_amount_one, select_currency_two, swap_currencies]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Select first currency
    select_currency_one(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_currency_one.png')
    
    # Input amount in the first currency
    input_amount_one(driver)
    driver.save_screenshot(f'{dir}/_images/after_input_amount_one.png')
    
    # Select second currency
    select_currency_two(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_currency_two.png')
    
    # Swap currencies
    swap_currencies(driver)
    driver.save_screenshot(f'{dir}/_images/after_swap_currencies.png')
    
    # Input amount in the second currency
    input_amount_two(driver)
    driver.save_screenshot(f'{dir}/_images/after_input_amount_two.png')
