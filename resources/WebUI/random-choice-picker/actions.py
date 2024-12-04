
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def enter_choices(driver):
    textarea = driver.find_element(By.ID, 'textarea')
    textarea.send_keys('Choice 1, Choice 2, Choice 3, Choice 4')
    time.sleep(1)  # Wait for the input to be processed

def press_enter(driver):
    textarea = driver.find_element(By.ID, 'textarea')
    textarea.send_keys('\n')
    time.sleep(2)  # Wait for the random selection process to complete

actions = [enter_choices, press_enter]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Enter choices
    enter_choices(driver)
    driver.save_screenshot(f'{dir}/_images/after_entering_choices.png')
    # Press enter to generate tags and start random selection
    press_enter(driver)
    driver.save_screenshot(f'{dir}/_images/after_random_selection.png')
