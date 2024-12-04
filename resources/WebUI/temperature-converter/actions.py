
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def input_celsius(driver):
    celsius_input = driver.find_element(By.ID, 'celsius')
    celsius_input.clear()
    celsius_input.send_keys('25')
    time.sleep(2)

def input_fahrenheit(driver):
    fahrenheit_input = driver.find_element(By.ID, 'fahrenheit')
    fahrenheit_input.clear()
    fahrenheit_input.send_keys('77')
    time.sleep(2)

def input_kelvin(driver):
    kelvin_input = driver.find_element(By.ID, 'kelvin')
    kelvin_input.clear()
    kelvin_input.send_keys('300')
    time.sleep(2)

actions = [input_celsius, input_fahrenheit, input_kelvin]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Input Celsius value
    input_celsius(driver)
    driver.save_screenshot(f'{dir}/_images/after_input_celsius.png')
    
    # Input Fahrenheit value
    input_fahrenheit(driver)
    driver.save_screenshot(f'{dir}/_images/after_input_fahrenheit.png')
    
    # Input Kelvin value
    input_kelvin(driver)
    driver.save_screenshot(f'{dir}/_images/after_input_kelvin.png')
