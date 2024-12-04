
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def type_text(driver):
    input_field = driver.find_element(By.ID, 'input-field')
    input_field.send_keys('Hello World')
    time.sleep(1)

def click_uppercase(driver):
    uppercase_button = driver.find_element(By.CSS_SELECTOR, '.btn.uppercase')
    uppercase_button.click()
    time.sleep(1)

def click_lowercase(driver):
    lowercase_button = driver.find_element(By.CSS_SELECTOR, '.btn.lowercase')
    lowercase_button.click()
    time.sleep(1)

def click_bold(driver):
    bold_button = driver.find_element(By.CSS_SELECTOR, '.btn.bold')
    bold_button.click()
    time.sleep(1)

def click_italic(driver):
    italic_button = driver.find_element(By.CSS_SELECTOR, '.btn.italic')
    italic_button.click()
    time.sleep(1)

actions = [type_text, click_uppercase, click_bold, click_italic]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Type text
    type_text(driver)
    driver.save_screenshot(f'{dir}/_images/after_typing.png')
    
    # Click uppercase button
    click_uppercase(driver)
    driver.save_screenshot(f'{dir}/_images/after_uppercase.png')
    
    # Click lowercase button
    click_lowercase(driver)
    driver.save_screenshot(f'{dir}/_images/after_lowercase.png')
    
    # Click bold button
    click_bold(driver)
    driver.save_screenshot(f'{dir}/_images/after_bold.png')
    
    # Click italic button
    click_italic(driver)
    driver.save_screenshot(f'{dir}/_images/after_italic.png')
