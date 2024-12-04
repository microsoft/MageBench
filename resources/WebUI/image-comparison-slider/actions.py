
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def drag_slider_to_left(driver):
    slider = driver.find_element(By.CLASS_NAME, 'slider')
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(-100, 0).release().perform()
    time.sleep(2)

def drag_slider_to_right(driver):
    slider = driver.find_element(By.CLASS_NAME, 'slider')
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(100, 0).release().perform()
    time.sleep(2)

actions = [drag_slider_to_left, drag_slider_to_right]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Drag slider to the left
    drag_slider_to_left(driver)
    # Save after dragging to the left
    driver.save_screenshot(f'{dir}/_images/after_drag_left.png') 
    # Drag slider to the right
    drag_slider_to_right(driver)
    # Save after dragging to the right
    driver.save_screenshot(f'{dir}/_images/after_drag_right.png') 
