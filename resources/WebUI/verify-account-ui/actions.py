
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def enter_first_digit(driver):
    first_input = driver.find_element(By.CSS_SELECTOR, '.code')
    first_input.send_keys('1')
    time.sleep(1)

def enter_second_digit(driver):
    second_input = driver.find_elements(By.CSS_SELECTOR, '.code')[1]
    second_input.send_keys('2')
    time.sleep(1)

def enter_third_digit(driver):
    third_input = driver.find_elements(By.CSS_SELECTOR, '.code')[2]
    third_input.send_keys('3')
    time.sleep(1)

def enter_fourth_digit(driver):
    fourth_input = driver.find_elements(By.CSS_SELECTOR, '.code')[3]
    fourth_input.send_keys('4')
    time.sleep(1)

def enter_fifth_digit(driver):
    fifth_input = driver.find_elements(By.CSS_SELECTOR, '.code')[4]
    fifth_input.send_keys('5')
    time.sleep(1)

actions = [enter_first_digit, enter_second_digit]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Perform actions
    for action in actions:
        action(driver)
        driver.save_screenshot(f'{dir}/_images/after_{action.__name__}.png')
