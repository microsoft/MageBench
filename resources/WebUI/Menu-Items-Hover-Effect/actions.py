
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_home(driver):
    element = driver.find_element(By.XPATH, "//a[@data-text='Home']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_about(driver):
    element = driver.find_element(By.XPATH, "//a[@data-text='About']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_services(driver):
    element = driver.find_element(By.XPATH, "//a[@data-text='Services']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_team(driver):
    element = driver.find_element(By.XPATH, "//a[@data-text='Team']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_contact(driver):
    element = driver.find_element(By.XPATH, "//a[@data-text='Contact']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

actions = [hover_home, hover_about, hover_services, hover_team, hover_contact]

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
    
    hover_team(driver)
    driver.save_screenshot(f'{dir}/_images/hover_team.png')
    
    hover_contact(driver)
    driver.save_screenshot(f'{dir}/_images/hover_contact.png')
