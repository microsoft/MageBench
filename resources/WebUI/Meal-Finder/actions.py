
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def search_meal(driver):
    search_input = driver.find_element(By.CLASS_NAME, 'input')
    search_input.send_keys('Chicken')
    search_input.submit()
    time.sleep(2)  # Wait for the search results to load

def click_magnifier(driver):
    magnifier_icon = driver.find_element(By.CLASS_NAME, 'magnifier')
    magnifier_icon.click()
    time.sleep(2)  # Wait for the search results to load

def click_breakfast(driver):
    breakfast_link = driver.find_element(By.XPATH, "//li[text()='Breakfast']")
    breakfast_link.click()
    time.sleep(2)  # Wait for the page to load

def click_lunch(driver):
    lunch_link = driver.find_element(By.XPATH, "//li[text()='Launch']")
    lunch_link.click()
    time.sleep(2)  # Wait for the page to load

def click_dinner(driver):
    dinner_link = driver.find_element(By.XPATH, "//li[text()='Dinner']")
    dinner_link.click()
    time.sleep(2)  # Wait for the page to load

actions = [search_meal]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Perform search meal action
    search_meal(driver)
    driver.save_screenshot(f'{dir}/_images/after_search_meal.png')
    
    # Click magnifier icon
    click_magnifier(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_magnifier.png')
    
    # Click Breakfast link
    click_breakfast(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_breakfast.png')
    
    # Click Lunch link
    click_lunch(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_lunch.png')
    
    # Click Dinner link
    click_dinner(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_dinner.png')
