
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def click_magic_button(driver):
    button = driver.find_element(By.ID, 'btn')
    button.click()
    time.sleep(1)  # Wait for the animation to complete

actions = [click_magic_button]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Click the magic button
    click_magic_button(driver)
    
    # Save after clicking the button
    driver.save_screenshot(f'{dir}/_images/after_click.png')
