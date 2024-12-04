
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_over_container(driver):
    container = driver.find_element(By.CLASS_NAME, 'container')
    actions = ActionChains(driver)
    actions.move_to_element(container).perform()
    time.sleep(2)  # wait for the hover effect to complete

actions = [hover_over_container]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Perform hover action
    hover_over_container(driver)
    # Save after hover
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
