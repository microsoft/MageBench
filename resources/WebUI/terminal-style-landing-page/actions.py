
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_about(driver):
    about_element = driver.find_element(By.ID, 'about')
    about_element.click()
    time.sleep(2)  # Wait for the modal to fully appear

def click_contact(driver):
    contact_element = driver.find_element(By.ID, 'contact')
    contact_element.click()
    time.sleep(2)  # Wait for the modal to fully appear

actions = [click_about, click_contact]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    
    # Click on the "About" link
    click_about(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_about.png') 
    
    # Click on the "Contact" link
    click_contact(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_contact.png') 
