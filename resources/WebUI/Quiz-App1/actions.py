
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_start_button(driver):
    start_button = driver.find_element(By.CLASS_NAME, 'startBtn')
    start_button.click()
    time.sleep(2)  # Wait for the quiz to start

def select_first_choice(driver):
    first_choice = driver.find_element(By.CLASS_NAME, 'choice')
    first_choice.click()
    time.sleep(1)  # Wait for the selection animation

def click_next_button(driver):
    next_button = driver.find_element(By.CLASS_NAME, 'nextBtn')
    next_button.click()
    time.sleep(2)  # Wait for the next question to load

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 

    # Click start button
    click_start_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_start.png') 

    # Select the first choice
    select_first_choice(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_choice.png') 

    # Click next button
    click_next_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_next.png') 

actions = [click_start_button, select_first_choice, click_next_button]
