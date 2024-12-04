
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for the scroll and animations to complete

actions = [scroll_down]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Scroll down to the bottom of the page
    scroll_down(driver)
    # Save after scrolling
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png') 
