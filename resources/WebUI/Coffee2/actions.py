
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_learn_more(driver):
    element = driver.find_element(By.XPATH, "//button[text()='Learn More']")
    element.click()
    time.sleep(1)  # Wait for any potential animations or page changes

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Click the "Learn More" button
    click_learn_more(driver)
    # Save after clicking the button
    driver.save_screenshot(f'{dir}/_images/after_click.png') 
