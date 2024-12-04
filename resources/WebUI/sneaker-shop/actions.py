
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_quarter_page(driver):
    driver.execute_script("window.scrollBy(0, arguments[0]);", 3863 / 4)
    time.sleep(2)

actions = [scroll_quarter_page, scroll_quarter_page, scroll_quarter_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll 1/4 of the page and save screenshot
    scroll_quarter_page(driver)
    driver.save_screenshot(f'{dir}/_images/scroll_1.png')
    
    # Scroll another 1/4 of the page and save screenshot
    scroll_quarter_page(driver)
    driver.save_screenshot(f'{dir}/_images/scroll_2.png')
    
    # Scroll another 1/4 of the page and save screenshot
    scroll_quarter_page(driver)
    driver.save_screenshot(f'{dir}/_images/scroll_3.png')
    
    # Scroll to the bottom of the page and save screenshot
    scroll_quarter_page(driver)
    driver.save_screenshot(f'{dir}/_images/scroll_4.png')
