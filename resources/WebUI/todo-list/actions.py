
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def add_todo_item(driver):
    input_field = driver.find_element(By.ID, 'input')
    input_field.send_keys('Test Todo')
    input_field.submit()
    time.sleep(2)  # Wait for the todo item to be added

def toggle_todo_item(driver):
    todo_item = driver.find_element(By.CSS_SELECTOR, '.todos>li')
    todo_item.click()
    time.sleep(2)  # Wait for the toggle action to complete

def delete_todo_item(driver):
    todo_item = driver.find_element(By.CSS_SELECTOR, '.todos>li')
    actions = ActionChains(driver)
    actions.context_click(todo_item).perform()
    time.sleep(2)  # Wait for the delete action to complete

actions = [add_todo_item, toggle_todo_item, delete_todo_item]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Add a todo item
    add_todo_item(driver)
    driver.save_screenshot(f'{dir}/_images/after_add.png')
    
    # Toggle the todo item
    toggle_todo_item(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle.png')
    
    # Delete the todo item
    delete_todo_item(driver)
    driver.save_screenshot(f'{dir}/_images/after_delete.png')
