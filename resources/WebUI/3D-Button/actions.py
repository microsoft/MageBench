
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def hover_over_button(driver):
    button = driver.find_element(By.CLASS_NAME, 'btn')
    actions = ActionChains(driver)
    actions.move_to_element(button).perform()
    time.sleep(1)  # Wait to capture the hover effect

actions = [hover_over_button]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    # Hover over the button
    hover_over_button(driver)
    # Save after hover
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
