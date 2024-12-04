
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_play_button(driver):
    play_button = driver.find_element(By.CLASS_NAME, 'btn')
    play_button.click()
    time.sleep(2)  # Wait for the trailer container to become visible

def click_close_icon(driver):
    close_icon = driver.find_element(By.CLASS_NAME, 'close-icon')
    close_icon.click()
    time.sleep(2)  # Wait for the trailer container to hide

actions = [click_play_button, click_close_icon]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the play button to show the trailer
    click_play_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_play_click.png')
    
    # Click the close icon to hide the trailer
    click_close_icon(driver)
    driver.save_screenshot(f'{dir}/_images/after_close_click.png')
