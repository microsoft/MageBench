
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_hamburger_menu(driver):
    element = driver.find_element(By.CLASS_NAME, 'hamburger-menu')
    element.click()
    time.sleep(2)  # wait for the menu to toggle

def interact(driver, dir):
    # save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # click hamburger menu
    click_hamburger_menu(driver)
    # save after clicking hamburger menu
    driver.save_screenshot(f'{dir}/_images/after_click_hamburger.png') 

actions = [click_hamburger_menu]
