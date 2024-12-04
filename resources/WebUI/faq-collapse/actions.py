
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_state(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def toggle_first_faq(driver):
    first_toggle = driver.find_elements(By.CLASS_NAME, 'faq-toggle')[0]
    first_toggle.click()
    time.sleep(1)

def toggle_second_faq(driver):
    second_toggle = driver.find_elements(By.CLASS_NAME, 'faq-toggle')[1]
    second_toggle.click()
    time.sleep(1)

def toggle_third_faq(driver):
    third_toggle = driver.find_elements(By.CLASS_NAME, 'faq-toggle')[2]
    third_toggle.click()
    time.sleep(1)

def toggle_fourth_faq(driver):
    fourth_toggle = driver.find_elements(By.CLASS_NAME, 'faq-toggle')[3]
    fourth_toggle.click()
    time.sleep(1)

def toggle_fifth_faq(driver):
    fifth_toggle = driver.find_elements(By.CLASS_NAME, 'faq-toggle')[4]
    fifth_toggle.click()
    time.sleep(1)

actions = [toggle_second_faq, toggle_third_faq, toggle_fourth_faq, toggle_fifth_faq]

def interact(driver, dir):
    # Save the original UI
    save_initial_state(driver, dir)
    
    # Toggle each FAQ and save the state after each toggle
    toggle_first_faq(driver)
    driver.save_screenshot(f'{dir}/_images/after_first_toggle.png')
    
    toggle_second_faq(driver)
    driver.save_screenshot(f'{dir}/_images/after_second_toggle.png')
    
    toggle_third_faq(driver)
    driver.save_screenshot(f'{dir}/_images/after_third_toggle.png')
    
    toggle_fourth_faq(driver)
    driver.save_screenshot(f'{dir}/_images/after_fourth_toggle.png')
    
    toggle_fifth_faq(driver)
    driver.save_screenshot(f'{dir}/_images/after_fifth_toggle.png')
