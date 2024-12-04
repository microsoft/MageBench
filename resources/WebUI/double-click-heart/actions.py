
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def double_click_image(driver):
    image = driver.find_element(By.CLASS_NAME, 'loveMe')
    actions = ActionChains(driver)
    actions.double_click(image).perform()
    time.sleep(1)  # Wait for the heart animation to complete

actions = [double_click_image]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Perform double-click on the image
    double_click_image(driver)
    # Save after double-click
    driver.save_screenshot(f'{dir}/_images/after_double_click.png')
