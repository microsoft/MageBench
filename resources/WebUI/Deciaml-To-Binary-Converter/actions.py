
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def enter_number(driver):
    number_input = driver.find_element(By.ID, 'number')
    number_input.send_keys('10')
    time.sleep(1)

def click_check_button(driver):
    check_button = driver.find_element(By.CLASS_NAME, 'result-btn')
    check_button.click()
    time.sleep(2)

actions = [enter_number, click_check_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Enter number
    enter_number(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_number.png')
    # Click check button
    click_check_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_check.png')
