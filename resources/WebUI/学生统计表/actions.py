
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def add_student_record(driver):
    driver.find_element(By.NAME, 'uname').send_keys('张三')
    driver.find_element(By.NAME, 'age').send_keys('25')
    driver.find_element(By.NAME, 'salary').send_keys('15000')
    driver.find_element(By.NAME, 'gender').send_keys('男')
    driver.find_element(By.NAME, 'city').send_keys('上海')
    driver.find_element(By.CLASS_NAME, 'add').click()
    time.sleep(2)  # Wait for the record to be added

def save_after_add_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/after_add.png')

def delete_student_record(driver):
    delete_button = driver.find_element(By.CSS_SELECTOR, 'tbody a')
    delete_button.click()
    time.sleep(1)  # Wait for the confirmation dialog

def save_after_delete_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/after_delete.png')

actions = [add_student_record, delete_student_record]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    # Add a new student record
    add_student_record(driver)
    # Save after adding a new record
    save_after_add_screenshot(driver, dir)
    # Delete the student record
    delete_student_record(driver)
    # Save after deleting the record
    save_after_delete_screenshot(driver, dir)
