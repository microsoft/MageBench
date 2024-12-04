
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def change_spacing(driver):
    spacing_input = driver.find_element(By.ID, 'spacing')
    spacing_input.clear()
    spacing_input.send_keys('50')
    time.sleep(2)

def change_blur(driver):
    blur_input = driver.find_element(By.ID, 'blur')
    blur_input.clear()
    blur_input.send_keys('15')
    time.sleep(2)

def change_color(driver):
    color_input = driver.find_element(By.ID, 'base')
    color_input.send_keys('#00ff00')
    time.sleep(2)

actions = [change_spacing, change_blur]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Change spacing
    change_spacing(driver)
    driver.save_screenshot(f'{dir}/_images/after_spacing.png')
    
    # Change blur
    change_blur(driver)
    driver.save_screenshot(f'{dir}/_images/after_blur.png')
    
    # Change color
    change_color(driver)
    driver.save_screenshot(f'{dir}/_images/after_color.png')
