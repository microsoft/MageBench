
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_get_started(driver):
    element = driver.find_element(By.CLASS_NAME, 'main-btn')
    element.click()
    time.sleep(2)  # Wait for any potential navigation or animation

def hover_over_card(driver):
    element_to_hover = driver.find_element(By.CLASS_NAME, 'cards__card')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)  # Wait to observe any hover effects

actions = [hover_over_card]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the "Get Started" button
    click_get_started(driver)
    driver.save_screenshot(f'{dir}/_images/after_click.png')
    
    # Hover over the first card
    hover_over_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
