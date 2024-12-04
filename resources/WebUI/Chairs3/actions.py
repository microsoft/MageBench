
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_on_first_card(driver):
    first_card = driver.find_elements(By.CLASS_NAME, 'card')[0]
    first_card.click()
    time.sleep(2)

def click_on_second_card(driver):
    second_card = driver.find_elements(By.CLASS_NAME, 'card')[1]
    second_card.click()
    time.sleep(2)

def click_on_third_card(driver):
    third_card = driver.find_elements(By.CLASS_NAME, 'card')[2]
    third_card.click()
    time.sleep(2)

def hover_over_first_card(driver):
    first_card = driver.find_elements(By.CLASS_NAME, 'card')[0]
    actions = ActionChains(driver)
    actions.move_to_element(first_card).perform()
    time.sleep(2)

def hover_over_second_card(driver):
    second_card = driver.find_elements(By.CLASS_NAME, 'card')[1]
    actions = ActionChains(driver)
    actions.move_to_element(second_card).perform()
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on the first card
    click_on_first_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_first_card.png')
    
    # Click on the second card
    click_on_second_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_second_card.png')
    
    # Click on the third card
    click_on_third_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_third_card.png')
    
    # Hover over the first card
    hover_over_first_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_first_card.png')
    
    # Hover over the second card
    hover_over_second_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_second_card.png')
