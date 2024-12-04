
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Scroll the page
    scroll_page(driver)
    # Save after scroll
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
