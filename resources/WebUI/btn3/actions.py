
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_over_link(driver):
    link_element = driver.find_element(By.TAG_NAME, 'a')
    actions = ActionChains(driver)
    actions.move_to_element(link_element).perform()
    time.sleep(1)  # Wait for the hover effect to complete

actions = [hover_over_link]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Hover over the link
    hover_over_link(driver)
    # Save after hover
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
