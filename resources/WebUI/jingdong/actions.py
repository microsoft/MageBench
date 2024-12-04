
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_over_image(driver):
    normal_div = driver.find_element(By.ID, 'normal')
    actions = ActionChains(driver)
    actions.move_to_element(normal_div).perform()
    time.sleep(2)  # Wait for the magnifying glass and larger image to appear

def move_mouse_within_image(driver):
    normal_div = driver.find_element(By.ID, 'normal')
    actions = ActionChains(driver)
    # Move to the center of the image
    actions.move_to_element_with_offset(normal_div, 200, 200).perform()
    time.sleep(1)
    # Move to the top-left corner
    actions.move_to_element_with_offset(normal_div, 50, 50).perform()
    time.sleep(1)
    # Move to the bottom-right corner
    actions.move_to_element_with_offset(normal_div, 350, 350).perform()
    time.sleep(1)

def move_mouse_outside_image(driver):
    normal_div = driver.find_element(By.ID, 'normal')
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(normal_div, -50, -50).perform()
    time.sleep(2)  # Wait for the magnifying glass and larger image to disappear

actions = [hover_over_image]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Hover over the image
    hover_over_image(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
    # Move the mouse within the image
    move_mouse_within_image(driver)
    driver.save_screenshot(f'{dir}/_images/after_move_within.png')
    # Move the mouse outside the image
    move_mouse_outside_image(driver)
    driver.save_screenshot(f'{dir}/_images/after_move_outside.png')
