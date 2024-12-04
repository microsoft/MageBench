
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def input_text(driver):
    text_area = driver.find_element(By.CLASS_NAME, 'text-input')
    text_area.send_keys("Hello world! This is a test input to check the word counter functionality.")
    time.sleep(2)

actions = [input_text]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png') 
    # Input text
    input_text(driver)
    driver.save_screenshot(f'{dir}/_images/after_input.png') 
