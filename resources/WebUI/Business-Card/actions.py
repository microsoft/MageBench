
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def hover_over_card(driver):
    card_element = driver.find_element(By.CLASS_NAME, 'card-wrapper')
    actions = ActionChains(driver)
    actions.move_to_element(card_element).perform()
    time.sleep(1)  # Wait for the flip animation to complete

actions = [hover_over_card]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    # Hover over the card to flip it
    hover_over_card(driver)
    # Save the screenshot after hover
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
