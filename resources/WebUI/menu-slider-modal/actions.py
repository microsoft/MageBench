
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def toggle_navbar(driver):
    toggle_button = driver.find_element(By.ID, 'toggle')
    toggle_button.click()
    time.sleep(2)

def open_modal(driver):
    open_button = driver.find_element(By.ID, 'open')
    open_button.click()
    time.sleep(2)

def close_modal(driver):
    close_button = driver.find_element(By.ID, 'close')
    close_button.click()
    time.sleep(2)

actions = [scroll_page, toggle_navbar, open_modal, close_modal]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Toggle the navigation menu
    toggle_navbar(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle_navbar.png')
    
    # Open the modal
    open_modal(driver)
    driver.save_screenshot(f'{dir}/_images/after_open_modal.png')
    
    # Close the modal
    close_modal(driver)
    driver.save_screenshot(f'{dir}/_images/after_close_modal.png')
