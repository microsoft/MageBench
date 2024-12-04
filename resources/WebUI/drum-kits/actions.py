
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_crash_button(driver):
    crash_button = driver.find_element(By.XPATH, "//button[text()='crash']")
    crash_button.click()
    time.sleep(1)

def click_kick_button(driver):
    kick_button = driver.find_element(By.XPATH, "//button[text()='kick']")
    kick_button.click()
    time.sleep(1)

def click_snare_button(driver):
    snare_button = driver.find_element(By.XPATH, "//button[text()='snare']")
    snare_button.click()
    time.sleep(1)

def click_tom_button(driver):
    tom_button = driver.find_element(By.XPATH, "//button[text()='tom']")
    tom_button.click()
    time.sleep(1)

def press_key_c(driver):
    actions = ActionChains(driver)
    actions.send_keys('c').perform()
    time.sleep(1)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click crash button
    click_crash_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_crash.png')
    
    # Click kick button
    click_kick_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_kick.png')
    
    # Click snare button
    click_snare_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_snare.png')
    
    # Click tom button
    click_tom_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_tom.png')
    
    # Press key 'c'
    press_key_c(driver)
    driver.save_screenshot(f'{dir}/_images/after_press_key_c.png')
