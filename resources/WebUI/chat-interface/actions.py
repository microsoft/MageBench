
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def type_message(driver):
    input_field = driver.find_element(By.CLASS_NAME, 'text_input')
    input_field.send_keys("This is a test message.")
    time.sleep(1)

actions = [type_message]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Type a message
    type_message(driver)
    # Save after typing the message
    driver.save_screenshot(f'{dir}/_images/after_typing.png')
