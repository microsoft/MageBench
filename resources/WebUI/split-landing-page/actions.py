
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_left(driver):
    left_section = driver.find_element(By.CLASS_NAME, 'left')
    actions = ActionChains(driver)
    actions.move_to_element(left_section).perform()
    time.sleep(2)

def hover_right(driver):
    right_section = driver.find_element(By.CLASS_NAME, 'right')
    actions = ActionChains(driver)
    actions.move_to_element(right_section).perform()
    time.sleep(2)

def click_left_button(driver):
    left_button = driver.find_element(By.CSS_SELECTOR, '.left .btn')
    left_button.click()
    time.sleep(2)

def click_right_button(driver):
    right_button = driver.find_element(By.CSS_SELECTOR, '.right .btn')
    right_button.click()
    time.sleep(2)

actions = [hover_left, hover_right]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Hover over the left section
    hover_left(driver)
    driver.save_screenshot(f'{dir}/_images/hover_left.png')
    
    # Hover over the right section
    hover_right(driver)
    driver.save_screenshot(f'{dir}/_images/hover_right.png')
    
    # Click the "Buy Now" button in the left section
    click_left_button(driver)
    driver.save_screenshot(f'{dir}/_images/click_left_button.png')
    
    # Click the "Buy Now" button in the right section
    click_right_button(driver)
    driver.save_screenshot(f'{dir}/_images/click_right_button.png')
