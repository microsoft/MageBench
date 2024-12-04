
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def enter_date_of_birth(driver):
    birthday_input = driver.find_element(By.ID, 'birthday')
    birthday_input.send_keys('001990-05-02')
    time.sleep(1)  # Wait for the input to be processed

def click_calculate_age(driver):
    calculate_button = driver.find_element(By.ID, 'btn')
    calculate_button.click()
    time.sleep(1)  # Wait for the result to be displayed

actions = [enter_date_of_birth, click_calculate_age]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Enter date of birth
    enter_date_of_birth(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_date.png')
    # Click calculate age button
    click_calculate_age(driver)
    driver.save_screenshot(f'{dir}/_images/after_calculate_age.png')
