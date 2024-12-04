
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def hover_web_development(driver):
    element = driver.find_element(By.XPATH, "//a[text()='Web Development']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_front_end(driver):
    element = driver.find_element(By.XPATH, "//a[text()='Front End']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_back_end(driver):
    element = driver.find_element(By.XPATH, "//a[text()='Back End']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

actions = [hover_web_development, hover_front_end, hover_back_end]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Hover over "Web Development"
    hover_web_development(driver)
    driver.save_screenshot(f'{dir}/_images/hover_web_development.png')
    
    # Hover over "Front End"
    hover_front_end(driver)
    driver.save_screenshot(f'{dir}/_images/hover_front_end.png')
    
    # Hover over "Back End"
    hover_back_end(driver)
    driver.save_screenshot(f'{dir}/_images/hover_back_end.png')
