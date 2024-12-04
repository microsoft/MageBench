
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_switch(driver):
    switch_button = driver.find_element(By.CLASS_NAME, 'btn')
    switch_button.click()
    time.sleep(2)  # Wait for the light to turn on and audio to play

actions = [click_switch]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Click the switch to turn on the light
    click_switch(driver)
    # Save after clicking the switch
    driver.save_screenshot(f'{dir}/_images/after_click.png') 
