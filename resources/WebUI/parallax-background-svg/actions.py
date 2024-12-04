
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Allow time for the parallax effect to be visible

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Scroll to see the parallax effect
    scroll_page(driver)
    # Save after scrolling
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
