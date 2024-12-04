
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_more_properties(driver):
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(2)  # Assuming there might be some animation or action

def click_first_dot(driver):
    first_dot = driver.find_elements(By.CLASS_NAME, 'btn')[0]
    first_dot.click()
    time.sleep(2)  # Wait for the image to change and animation to complete

def click_second_dot(driver):
    second_dot = driver.find_elements(By.CLASS_NAME, 'btn')[1]
    second_dot.click()
    time.sleep(2)  # Wait for the image to change and animation to complete

def click_third_dot(driver):
    third_dot = driver.find_elements(By.CLASS_NAME, 'btn')[2]
    third_dot.click()
    time.sleep(2)  # Wait for the image to change and animation to complete

actions = [click_second_dot, click_third_dot]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    
    # Click "More Properties" button
    click_more_properties(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_more_properties.png') 
    
    # Click first dot
    click_first_dot(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_first_dot.png') 
    
    # Click second dot
    click_second_dot(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_second_dot.png') 
    
    # Click third dot
    click_third_dot(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_third_dot.png') 
