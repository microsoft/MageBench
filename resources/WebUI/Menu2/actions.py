
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_home(driver):
    home_element = driver.find_element(By.XPATH, "//a[text()='Home']")
    actions = ActionChains(driver)
    actions.move_to_element(home_element).perform()
    time.sleep(2)

def hover_about(driver):
    about_element = driver.find_element(By.XPATH, "//a[text()='About']")
    actions = ActionChains(driver)
    actions.move_to_element(about_element).perform()
    time.sleep(2)

actions = [hover_home, hover_about]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Hover over Home
    hover_home(driver)
    driver.save_screenshot(f'{dir}/_images/hover_home.png')
    # Hover over About
    hover_about(driver)
    driver.save_screenshot(f'{dir}/_images/hover_about.png')
