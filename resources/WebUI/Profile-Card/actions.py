
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_contact_me_button(driver):
    button = driver.find_element(By.CLASS_NAME, 'card-btn')
    button.click()
    time.sleep(2)  # Wait for the animation to complete

actions = [click_contact_me_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Click the "Contact Me" button
    click_contact_me_button(driver)
    # Save after clicking the button
    driver.save_screenshot(f'{dir}/_images/after_click.png') 
