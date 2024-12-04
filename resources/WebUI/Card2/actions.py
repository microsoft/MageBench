
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_over_card(driver):
    card_element = driver.find_element(By.CLASS_NAME, 'card')
    actions = ActionChains(driver)
    actions.move_to_element(card_element).perform()
    time.sleep(1)  # Wait for the hover animation to complete

actions = [hover_over_card]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Hover over the card
    hover_over_card(driver)
    # Save after hover
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
