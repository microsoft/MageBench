
from selenium.webdriver.common.by import By
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Scroll to view the entire content
    scroll_page(driver)
    # Save after scrolling
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
