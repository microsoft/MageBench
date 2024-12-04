
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def increase_brush_size(driver):
    increase_button = driver.find_element(By.ID, 'increase')
    increase_button.click()
    time.sleep(1)

def decrease_brush_size(driver):
    decrease_button = driver.find_element(By.ID, 'decrease')
    decrease_button.click()
    time.sleep(1)

def change_brush_color(driver):
    color_picker = driver.find_element(By.ID, 'color')
    color_picker.send_keys('#ff0000')  # Change color to red
    time.sleep(1)

def draw_on_canvas(driver):
    canvas = driver.find_element(By.ID, 'canvas')
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(canvas, 100, 100).click_and_hold().move_by_offset(50, 50).release().perform()
    time.sleep(1)

def clear_canvas(driver):
    clear_button = driver.find_element(By.ID, 'clear')
    clear_button.click()
    time.sleep(1)

actions = [increase_brush_size, decrease_brush_size, change_brush_color, draw_on_canvas, clear_canvas]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Increase brush size
    increase_brush_size(driver)
    driver.save_screenshot(f'{dir}/_images/after_increase_brush_size.png')
    
    # Decrease brush size
    decrease_brush_size(driver)
    driver.save_screenshot(f'{dir}/_images/after_decrease_brush_size.png')
    
    # Change brush color
    change_brush_color(driver)
    driver.save_screenshot(f'{dir}/_images/after_change_brush_color.png')
    
    # Draw on canvas
    draw_on_canvas(driver)
    driver.save_screenshot(f'{dir}/_images/after_draw_on_canvas.png')
    
    # Clear canvas
    clear_canvas(driver)
    driver.save_screenshot(f'{dir}/_images/after_clear_canvas.png')
