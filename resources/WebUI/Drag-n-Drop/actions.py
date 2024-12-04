
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def drag_and_drop(driver):
    # Locate the draggable element and the target empty container
    draggable = driver.find_element(By.CLASS_NAME, 'fill')
    target = driver.find_elements(By.CLASS_NAME, 'empty')[-1]  # Last empty container

    # Perform drag and drop
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, target).perform()
    time.sleep(2)  # Wait for the drop action to complete

actions = [drag_and_drop]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Perform drag and drop
    drag_and_drop(driver)
    # Save after drag and drop
    driver.save_screenshot(f'{dir}/_images/after_drag_and_drop.png') 
