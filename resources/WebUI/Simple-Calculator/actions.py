
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def input_number1(driver):
    num1_field = driver.find_element(By.CLASS_NAME, 'num1')
    num1_field.send_keys('10')
    time.sleep(1)

def input_number2(driver):
    num2_field = driver.find_element(By.CLASS_NAME, 'num2')
    num2_field.send_keys('5')
    time.sleep(1)

def select_operation(driver):
    select_op = driver.find_element(By.ID, 'selectOp')
    for option in select_op.find_elements(By.TAG_NAME, 'option'):
        if option.text == '+':
            option.click()
            break
    time.sleep(1)

def click_submit(driver):
    submit_button = driver.find_element(By.ID, 'btn')
    submit_button.click()
    time.sleep(2)  # Wait for the result to be displayed

actions = [input_number1, input_number2, select_operation, click_submit]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Input first number
    input_number1(driver)
    driver.save_screenshot(f'{dir}/_images/after_input_number1.png') 
    # Input second number
    input_number2(driver)
    driver.save_screenshot(f'{dir}/_images/after_input_number2.png') 
    # Select operation
    select_operation(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_operation.png') 
    # Click submit
    click_submit(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_submit.png') 
