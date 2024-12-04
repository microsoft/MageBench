
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_state(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def hover_over_today(driver):
    today_element = driver.find_element(By.CLASS_NAME, 'today')
    actions = ActionChains(driver)
    actions.move_to_element(today_element).perform()
    time.sleep(2)

def hover_over_first_day(driver):
    first_day_element = driver.find_element(By.CSS_SELECTOR, '.days div:not(.empty)')
    actions = ActionChains(driver)
    actions.move_to_element(first_day_element).perform()
    time.sleep(2)

actions = [hover_over_first_day]

def interact(driver, dir):
    # Save the initial state of the webpage
    save_initial_state(driver, dir)
    
    # Hover over the current day
    hover_over_today(driver)
    driver.save_screenshot(f'{dir}/_images/hover_today.png')
    
    # Hover over the first day of the month
    hover_over_first_day(driver)
    driver.save_screenshot(f'{dir}/_images/hover_first_day.png')
