
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_clear(driver):
    clear_button = driver.find_element(By.CLASS_NAME, 'clear')
    clear_button.click()
    time.sleep(1)

def click_seven(driver):
    seven_button = driver.find_element(By.XPATH, "//span[text()='7']")
    seven_button.click()
    time.sleep(1)

def click_plus(driver):
    plus_button = driver.find_element(By.CLASS_NAME, 'plus')
    plus_button.click()
    time.sleep(1)

def click_eight(driver):
    eight_button = driver.find_element(By.XPATH, "//span[text()='8']")
    eight_button.click()
    time.sleep(1)

def click_equal(driver):
    equal_button = driver.find_element(By.CLASS_NAME, 'equal')
    equal_button.click()
    time.sleep(1)

actions = [click_seven, click_plus, click_eight, click_equal, click_clear]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Perform actions
    click_clear(driver)
    driver.save_screenshot(f'{dir}/_images/after_clear.png')
    
    click_seven(driver)
    driver.save_screenshot(f'{dir}/_images/after_seven.png')
    
    click_plus(driver)
    driver.save_screenshot(f'{dir}/_images/after_plus.png')
    
    click_eight(driver)
    driver.save_screenshot(f'{dir}/_images/after_eight.png')
    
    click_equal(driver)
    driver.save_screenshot(f'{dir}/_images/after_equal.png')
