
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_on_thumb(driver):
    thumb_element = driver.find_element(By.CLASS_NAME, 'thumb')
    thumb_element.click()
    time.sleep(1)  # wait for the animation to complete

actions = [click_on_thumb]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Click on the thumb to toggle the light
    click_on_thumb(driver)
    # Save after clicking
    driver.save_screenshot(f'{dir}/_images/after_click.png')
