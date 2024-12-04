
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_learn_more_first_card(driver):
    element = driver.find_elements(By.TAG_NAME, 'button')[0]
    element.click()
    time.sleep(1)  # Assuming there might be some animation or page change

def click_learn_more_second_card(driver):
    element = driver.find_elements(By.TAG_NAME, 'button')[1]
    element.click()
    time.sleep(1)

def click_learn_more_third_card(driver):
    element = driver.find_elements(By.TAG_NAME, 'button')[2]
    element.click()
    time.sleep(1)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 

    # Click "Learn More" on the first card
    click_learn_more_first_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_first_card.png') 

    # Click "Learn More" on the second card
    click_learn_more_second_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_second_card.png') 

    # Click "Learn More" on the third card
    click_learn_more_third_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_third_card.png') 
