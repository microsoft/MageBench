
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_first_cup(driver):
    first_cup = driver.find_element(By.CSS_SELECTOR, '.cup-small:nth-child(1)')
    first_cup.click()
    time.sleep(1)

def click_second_cup(driver):
    second_cup = driver.find_element(By.CSS_SELECTOR, '.cup-small:nth-child(2)')
    second_cup.click()
    time.sleep(1)

def click_third_cup(driver):
    third_cup = driver.find_element(By.CSS_SELECTOR, '.cup-small:nth-child(3)')
    third_cup.click()
    time.sleep(1)

def click_fourth_cup(driver):
    fourth_cup = driver.find_element(By.CSS_SELECTOR, '.cup-small:nth-child(4)')
    fourth_cup.click()
    time.sleep(1)

def click_fifth_cup(driver):
    fifth_cup = driver.find_element(By.CSS_SELECTOR, '.cup-small:nth-child(5)')
    fifth_cup.click()
    time.sleep(1)

actions = [click_first_cup, click_fifth_cup]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 

    # Perform actions and save screenshots after each action
    for i, action in enumerate(actions):
        action(driver)
        driver.save_screenshot(f'{dir}/_images/after_action_{i+1}.png')
