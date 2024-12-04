
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_on_first_question(driver):
    element = driver.find_element(By.CSS_SELECTOR, 'label[for="first"]')
    element.click()
    time.sleep(1)

def click_on_second_question(driver):
    element = driver.find_element(By.CSS_SELECTOR, 'label[for="second"]')
    element.click()
    time.sleep(1)

def click_on_third_question(driver):
    element = driver.find_element(By.CSS_SELECTOR, 'label[for="third"]')
    element.click()
    time.sleep(1)

def click_on_fourth_question(driver):
    element = driver.find_element(By.CSS_SELECTOR, 'label[for="fourth"]')
    element.click()
    time.sleep(1)

def click_on_fifth_question(driver):
    element = driver.find_element(By.CSS_SELECTOR, 'label[for="fifth"]')
    element.click()
    time.sleep(1)

actions = [
    click_on_second_question,
    click_on_third_question,
    click_on_fourth_question,
    click_on_fifth_question
]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on the first question
    click_on_first_question(driver)
    driver.save_screenshot(f'{dir}/_images/after_first_click.png')
    
    # Click on the second question
    click_on_second_question(driver)
    driver.save_screenshot(f'{dir}/_images/after_second_click.png')
    
    # Click on the third question
    click_on_third_question(driver)
    driver.save_screenshot(f'{dir}/_images/after_third_click.png')
    
    # Click on the fourth question
    click_on_fourth_question(driver)
    driver.save_screenshot(f'{dir}/_images/after_fourth_click.png')
    
    # Click on the fifth question
    click_on_fifth_question(driver)
    driver.save_screenshot(f'{dir}/_images/after_fifth_click.png')
