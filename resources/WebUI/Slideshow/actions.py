
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_pause_button(driver):
    pause_button = driver.find_element(By.CLASS_NAME, 'play-pause')
    pause_button.click()
    time.sleep(2)  # wait for 3 seconds as per the requirement

def click_left_arrow(driver):
    left_arrow = driver.find_element(By.CLASS_NAME, 'left-arrow')
    left_arrow.click()
    time.sleep(1)  # wait for the slide transition

def click_right_arrow(driver):
    right_arrow = driver.find_element(By.CLASS_NAME, 'right-arrow')
    right_arrow.click()
    time.sleep(1)  # wait for the slide transition

actions = [click_pause_button, click_left_arrow, click_right_arrow]

def interact(driver, dir):
    # save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # click pause button
    click_pause_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_pause.png') 
    # click left arrow
    click_left_arrow(driver)
    driver.save_screenshot(f'{dir}/_images/after_left_arrow.png') 
    # click right arrow
    click_right_arrow(driver)
    driver.save_screenshot(f'{dir}/_images/after_right_arrow.png') 
