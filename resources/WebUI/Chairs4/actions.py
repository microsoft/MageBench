
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def hover_on_first_card(driver):
    first_card = driver.find_element(By.CSS_SELECTOR, '.card:nth-child(1)')
    actions = ActionChains(driver)
    actions.move_to_element(first_card).perform()
    time.sleep(1)

def hover_on_second_card(driver):
    second_card = driver.find_element(By.CSS_SELECTOR, '.card:nth-child(2)')
    actions = ActionChains(driver)
    actions.move_to_element(second_card).perform()
    time.sleep(1)

def hover_on_third_card(driver):
    third_card = driver.find_element(By.CSS_SELECTOR, '.card:nth-child(3)')
    actions = ActionChains(driver)
    actions.move_to_element(third_card).perform()
    time.sleep(1)

def hover_on_fourth_card(driver):
    fourth_card = driver.find_element(By.CSS_SELECTOR, '.card:nth-child(4)')
    actions = ActionChains(driver)
    actions.move_to_element(fourth_card).perform()
    time.sleep(1)

actions = []

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Hover over the first card
    hover_on_first_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_first_card.png')
    
    # Hover over the second card
    hover_on_second_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_second_card.png')
    
    # Hover over the third card
    hover_on_third_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_third_card.png')
    
    # Hover over the fourth card
    hover_on_fourth_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_fourth_card.png')
