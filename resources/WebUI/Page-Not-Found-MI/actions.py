
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_over_button(driver):
    button = driver.find_element(By.CLASS_NAME, 'button')
    actions = ActionChains(driver)
    actions.move_to_element(button).perform()
    time.sleep(2)

actions = [hover_over_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Hover over the button
    hover_over_button(driver)
    # Save after hover
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
