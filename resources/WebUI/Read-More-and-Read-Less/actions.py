
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_learn_more(driver):
    button = driver.find_element(By.CLASS_NAME, 'btn')
    button.click()
    time.sleep(2)  # wait for the toggle animation to complete

actions = [click_learn_more]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Click the "Learn More" button
    click_learn_more(driver)
    # Save after clicking the button
    driver.save_screenshot(f'{dir}/_images/after_click.png')
