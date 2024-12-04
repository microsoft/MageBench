
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def enter_username(driver):
    search_input = driver.find_element(By.ID, 'search')
    search_input.send_keys('octocat')  # Example GitHub username
    time.sleep(1)

def submit_form(driver):
    form = driver.find_element(By.ID, 'form')
    form.submit()
    time.sleep(2)  # Wait for the profile information to load

actions = [enter_username, submit_form]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Enter username
    enter_username(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_username.png') 
    # Submit form
    submit_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit_form.png') 
