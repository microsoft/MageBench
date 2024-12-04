
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_home_icon(driver):
    home_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link.change')
    home_icon.click()
    time.sleep(1)

def click_camera_icon(driver):
    camera_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link:nth-child(3)')
    camera_icon.click()
    time.sleep(1)

def click_calendar_icon(driver):
    calendar_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link:nth-child(4)')
    calendar_icon.click()
    time.sleep(1)

def click_compass_icon(driver):
    compass_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link:nth-child(5)')
    compass_icon.click()
    time.sleep(1)

def click_book_icon(driver):
    book_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link:nth-child(6)')
    book_icon.click()
    time.sleep(1)

actions = [click_camera_icon, click_calendar_icon]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Perform actions and save screenshots
    for action in actions:
        action(driver)
        driver.save_screenshot(f'{dir}/_images/after_{action.__name__}.png')
