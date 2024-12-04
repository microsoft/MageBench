
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_over_first_card(driver):
    first_card = driver.find_element(By.CSS_SELECTOR, '.container .card:first-child')
    actions = ActionChains(driver)
    actions.move_to_element(first_card).perform()
    time.sleep(2)

def hover_over_second_card(driver):
    second_card = driver.find_element(By.CSS_SELECTOR, '.container .card:nth-child(2)')
    actions = ActionChains(driver)
    actions.move_to_element(second_card).perform()
    time.sleep(2)

def hover_over_third_card(driver):
    third_card = driver.find_element(By.CSS_SELECTOR, '.container .card:nth-child(3)')
    actions = ActionChains(driver)
    actions.move_to_element(third_card).perform()
    time.sleep(2)

def hover_over_fourth_card(driver):
    fourth_card = driver.find_element(By.CSS_SELECTOR, '.container .card:nth-child(4)')
    actions = ActionChains(driver)
    actions.move_to_element(fourth_card).perform()
    time.sleep(2)

def hover_over_fifth_card(driver):
    fifth_card = driver.find_element(By.CSS_SELECTOR, '.container .card:nth-child(5)')
    actions = ActionChains(driver)
    actions.move_to_element(fifth_card).perform()
    time.sleep(2)

actions = [hover_over_first_card, hover_over_second_card, hover_over_third_card, hover_over_fourth_card, hover_over_fifth_card]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Hover over each card and save the screenshot
    hover_over_first_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_first_card.png')
    
    hover_over_second_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_second_card.png')
    
    hover_over_third_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_third_card.png')
    
    hover_over_fourth_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_fourth_card.png')
    
    hover_over_fifth_card(driver)
    driver.save_screenshot(f'{dir}/_images/hover_fifth_card.png')
