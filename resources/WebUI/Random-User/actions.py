
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def click_random_person_button(driver):
    button = driver.find_element(By.ID, 'btn')
    button.click()
    time.sleep(2)  # Wait for the new user data to load

actions = [click_random_person_button]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Click the button to fetch a random person
    click_random_person_button(driver)
    
    # Save the UI after fetching a new random person
    driver.save_screenshot(f'{dir}/_images/after_click.png')
