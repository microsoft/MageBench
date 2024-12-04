
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_on_door(driver):
    door = driver.find_element(By.CLASS_NAME, 'door')
    door.click()
    time.sleep(2)  # Wait for the door animation to complete

def hover_over_top_window(driver):
    top_window = driver.find_element(By.CLASS_NAME, 'top-window')
    actions = ActionChains(driver)
    actions.move_to_element(top_window).perform()
    time.sleep(2)  # Wait for the window animation to complete

actions = [click_on_door, hover_over_top_window]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Click on the door
    click_on_door(driver)
    # Save after clicking the door
    driver.save_screenshot(f'{dir}/_images/after_click_door.png')
    # Hover over the top window
    hover_over_top_window(driver)
    # Save after hovering over the top window
    driver.save_screenshot(f'{dir}/_images/after_hover_top_window.png')
