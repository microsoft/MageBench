
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_on_top_tooltip(driver):
    element = driver.find_element(By.CLASS_NAME, 'top')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

def hover_on_right_tooltip(driver):
    element = driver.find_element(By.CLASS_NAME, 'right')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

def hover_on_left_tooltip(driver):
    element = driver.find_element(By.CLASS_NAME, 'left')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

def hover_on_bottom_tooltip(driver):
    element = driver.find_element(By.CLASS_NAME, 'bottom')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

actions = [hover_on_top_tooltip, hover_on_right_tooltip, hover_on_left_tooltip, hover_on_bottom_tooltip]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Hover over top tooltip
    hover_on_top_tooltip(driver)
    driver.save_screenshot(f'{dir}/_images/hover_top.png')
    
    # Hover over right tooltip
    hover_on_right_tooltip(driver)
    driver.save_screenshot(f'{dir}/_images/hover_right.png')
    
    # Hover over left tooltip
    hover_on_left_tooltip(driver)
    driver.save_screenshot(f'{dir}/_images/hover_left.png')
    
    # Hover over bottom tooltip
    hover_on_bottom_tooltip(driver)
    driver.save_screenshot(f'{dir}/_images/hover_bottom.png')
