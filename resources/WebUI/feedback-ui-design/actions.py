
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_unhappy_rating(driver):
    element = driver.find_elements(By.CLASS_NAME, 'rating')[0]
    element.click()
    time.sleep(1)

def click_neutral_rating(driver):
    element = driver.find_elements(By.CLASS_NAME, 'rating')[1]
    element.click()
    time.sleep(1)

def click_satisfied_rating(driver):
    element = driver.find_elements(By.CLASS_NAME, 'rating')[2]
    element.click()
    time.sleep(1)

def click_send_review(driver):
    element = driver.find_element(By.ID, 'send')
    element.click()
    time.sleep(1)

actions = [click_unhappy_rating, click_neutral_rating, click_satisfied_rating, click_send_review]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on "Unhappy" rating
    click_unhappy_rating(driver)
    driver.save_screenshot(f'{dir}/_images/unhappy_selected.png')
    
    # Click on "Neutral" rating
    click_neutral_rating(driver)
    driver.save_screenshot(f'{dir}/_images/neutral_selected.png')
    
    # Click on "Satisfied" rating
    click_satisfied_rating(driver)
    driver.save_screenshot(f'{dir}/_images/satisfied_selected.png')
    
    # Click on "Send Review" button
    click_send_review(driver)
    driver.save_screenshot(f'{dir}/_images/review_sent.png')
