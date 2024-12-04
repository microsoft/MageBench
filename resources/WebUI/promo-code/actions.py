
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def hover_over_present(driver):
    present = driver.find_element(By.ID, 'present')
    actions = ActionChains(driver)
    actions.move_to_element(present).perform()
    time.sleep(2)  # Wait for the animation and confetti effect

actions = [hover_over_present]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    # Hover over the present
    hover_over_present(driver)
    # Save after hover
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
