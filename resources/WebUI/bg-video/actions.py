
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_over_title(driver):
    title_element = driver.find_element(By.CSS_SELECTOR, '.content h1')
    actions = ActionChains(driver)
    actions.move_to_element(title_element).perform()
    time.sleep(1)

def hover_over_button(driver):
    button_element = driver.find_element(By.CSS_SELECTOR, '.content a')
    actions = ActionChains(driver)
    actions.move_to_element(button_element).perform()
    time.sleep(1)

actions = [hover_over_title, hover_over_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Hover over the title
    hover_over_title(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_title.png')
    # Hover over the button
    hover_over_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_button.png')
