
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_home(driver):
    element = driver.find_element(By.LINK_TEXT, 'Home')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

def hover_about(driver):
    element = driver.find_element(By.LINK_TEXT, 'About')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

def hover_services(driver):
    element = driver.find_element(By.LINK_TEXT, 'Services')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

def hover_portfolio(driver):
    element = driver.find_element(By.LINK_TEXT, 'Portfolio')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

def hover_contact(driver):
    element = driver.find_element(By.LINK_TEXT, 'Contact')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)

actions = [hover_home, hover_about]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Hover over each menu item and save the screenshot
    hover_home(driver)
    driver.save_screenshot(f'{dir}/_images/hover_home.png')
    
    hover_about(driver)
    driver.save_screenshot(f'{dir}/_images/hover_about.png')
    
    hover_services(driver)
    driver.save_screenshot(f'{dir}/_images/hover_services.png')
    
    hover_portfolio(driver)
    driver.save_screenshot(f'{dir}/_images/hover_portfolio.png')
    
    hover_contact(driver)
    driver.save_screenshot(f'{dir}/_images/hover_contact.png')
