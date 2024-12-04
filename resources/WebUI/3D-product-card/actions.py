
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
