
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def move_mouse(driver):
    action = ActionChains(driver)
    # Move to the center of the screen
    action.move_by_offset(500, 500).perform()
    time.sleep(2)

actions = [move_mouse]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    # Move mouse to update coordinates
    move_mouse(driver)
    driver.save_screenshot(f'{dir}/_images/after_mouse_move.png')
