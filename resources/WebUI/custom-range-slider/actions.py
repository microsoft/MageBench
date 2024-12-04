
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def move_slider(driver):
    slider = driver.find_element(By.ID, 'range')
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(150, 0).release().perform()
    time.sleep(2)  # Allow time for the label to update

actions = [move_slider]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Move the slider
    move_slider(driver)
    # Save after moving the slider
    driver.save_screenshot(f'{dir}/_images/after_move_slider.png') 
