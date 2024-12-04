
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def change_color(driver):
    color_picker = driver.find_element(By.CSS_SELECTOR, 'input[type="color"]')
    color_picker.send_keys('#ff0000')  # Change color to red
    time.sleep(1)

def toggle_checkboxes(driver):
    checkboxes = driver.find_elements(By.CSS_SELECTOR, '.checkboxes input[type="checkbox"]')
    for checkbox in checkboxes:
        checkbox.click()
        time.sleep(1)

def toggle_radio_buttons(driver):
    radio_buttons = driver.find_elements(By.CSS_SELECTOR, '.radio-buttons input[type="radio"]')
    for radio in radio_buttons:
        radio.click()
        time.sleep(1)

def adjust_range_slider(driver):
    range_slider = driver.find_element(By.CSS_SELECTOR, '.range input[type="range"]')
    actions = ActionChains(driver)
    actions.click_and_hold(range_slider).move_by_offset(30, 0).release().perform()
    time.sleep(1)

actions = [change_color, toggle_checkboxes, toggle_radio_buttons, adjust_range_slider]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Change color
    change_color(driver)
    driver.save_screenshot(f'{dir}/_images/after_color_change.png')
    
    # Toggle checkboxes
    toggle_checkboxes(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle_checkboxes.png')
    
    # Toggle radio buttons
    toggle_radio_buttons(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle_radio_buttons.png')
    
    # Adjust range slider
    adjust_range_slider(driver)
    driver.save_screenshot(f'{dir}/_images/after_adjust_range_slider.png')
