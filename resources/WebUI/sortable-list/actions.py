
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def drag_and_drop(driver, from_index, to_index):
    list_items = driver.find_elements(By.CSS_SELECTOR, '.draggable-list li .draggable')
    source = list_items[from_index]
    target = list_items[to_index]
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    time.sleep(1)  # wait for the drag-and-drop action to complete

def click_check_order(driver):
    check_button = driver.find_element(By.ID, 'check')
    check_button.click()
    time.sleep(1)  # wait for the check order action to complete

def dg(driver):
    drag_and_drop(driver, 0, 6)
    drag_and_drop(driver, 1, 4)
    drag_and_drop(driver, 2, 8)
    drag_and_drop(driver, 3, 0)
    drag_and_drop(driver, 4, 2)

actions = [dg, click_check_order]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Perform drag-and-drop actions
    drag_and_drop(driver, 0, 6)  # Example: Move the first item to the seventh position
    driver.save_screenshot(f'{dir}/_images/after_drag_1.png')
    
    drag_and_drop(driver, 1, 4)  # Example: Move the second item to the fifth position
    driver.save_screenshot(f'{dir}/_images/after_drag_2.png')
    
    drag_and_drop(driver, 2, 8)  # Example: Move the third item to the ninth position
    driver.save_screenshot(f'{dir}/_images/after_drag_3.png')
    
    drag_and_drop(driver, 3, 0)  # Example: Move the fourth item to the first position
    driver.save_screenshot(f'{dir}/_images/after_drag_4.png')
    
    drag_and_drop(driver, 4, 2)  # Example: Move the fifth item to the third position
    driver.save_screenshot(f'{dir}/_images/after_drag_5.png')
    
    # Click the "Check Order" button
    click_check_order(driver)
    driver.save_screenshot(f'{dir}/_images/after_check.png')
