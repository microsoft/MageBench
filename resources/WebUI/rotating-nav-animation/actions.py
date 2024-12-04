
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_open_button(driver):
    open_button = driver.find_element(By.ID, 'open')
    open_button.click()
    time.sleep(2)

def click_close_button(driver):
    close_button = driver.find_element(By.ID, 'close')
    close_button.click()
    time.sleep(2)

actions = [scroll_page, click_open_button, click_close_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click open button
    click_open_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_open.png')
    
    # Click close button
    click_close_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_close.png')
