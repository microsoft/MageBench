
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_over_first_cell(driver):
    element_to_hover = driver.find_element(By.CSS_SELECTOR, '.container > div:nth-of-type(1)')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)

def hover_over_sixth_cell(driver):
    element_to_hover = driver.find_element(By.CSS_SELECTOR, '.container > div:nth-of-type(6)')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)

def hover_over_ninth_cell(driver):
    element_to_hover = driver.find_element(By.CSS_SELECTOR, '.container > div:nth-of-type(9)')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)

def hover_over_tenth_cell(driver):
    element_to_hover = driver.find_element(By.CSS_SELECTOR, '.container > div:nth-of-type(10)')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)

def hover_over_twelfth_cell(driver):
    element_to_hover = driver.find_element(By.CSS_SELECTOR, '.container > div:nth-of-type(12)')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)

actions = [hover_over_first_cell, hover_over_sixth_cell, hover_over_ninth_cell]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Hover over the first cell
    hover_over_first_cell(driver)
    driver.save_screenshot(f'{dir}/_images/hover_first_cell.png')
    
    # Hover over the sixth cell
    hover_over_sixth_cell(driver)
    driver.save_screenshot(f'{dir}/_images/hover_sixth_cell.png')
    
    # Hover over the ninth cell
    hover_over_ninth_cell(driver)
    driver.save_screenshot(f'{dir}/_images/hover_ninth_cell.png')
    
    # Hover over the tenth cell
    hover_over_tenth_cell(driver)
    driver.save_screenshot(f'{dir}/_images/hover_tenth_cell.png')
    
    # Hover over the twelfth cell
    hover_over_twelfth_cell(driver)
    driver.save_screenshot(f'{dir}/_images/hover_twelfth_cell.png')
