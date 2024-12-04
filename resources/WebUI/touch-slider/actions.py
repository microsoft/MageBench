
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def slide_to_next(driver):
    slider = driver.find_element(By.CLASS_NAME, 'slider-container')
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(-300, 0).release().perform()
    time.sleep(2)

def slide_to_previous(driver):
    slider = driver.find_element(By.CLASS_NAME, 'slider-container')
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(300, 0).release().perform()
    time.sleep(2)

def click_buy_now(driver):
    buy_now_button = driver.find_element(By.CSS_SELECTOR, '.slide:nth-child(1) .btn')
    buy_now_button.click()
    time.sleep(2)

actions = [slide_to_next, slide_to_previous]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Slide to the next item
    slide_to_next(driver)
    driver.save_screenshot(f'{dir}/_images/after_slide_next.png')
    
    # Slide back to the previous item
    slide_to_previous(driver)
    driver.save_screenshot(f'{dir}/_images/after_slide_previous.png')
    
    # Click on the "Buy Now" button
    click_buy_now(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_buy_now.png')
