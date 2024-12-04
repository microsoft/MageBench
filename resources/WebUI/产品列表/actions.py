
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def verify_email_links(driver):
    email_links = driver.find_elements(By.CSS_SELECTOR, '.content a')
    for link in email_links:
        print(link.text)  # Just to verify the links are present
    time.sleep(2)

def verify_games_links(driver):
    games_links = driver.find_elements(By.CSS_SELECTOR, '.games a')
    for link in games_links:
        print(link.text)  # Just to verify the links are present
    time.sleep(2)

def verify_bo_links(driver):
    bo_links = driver.find_elements(By.CSS_SELECTOR, '.bo a')
    for link in bo_links:
        print(link.text)  # Just to verify the links are present
    time.sleep(2)

def verify_cai_links(driver):
    cai_links = driver.find_elements(By.CSS_SELECTOR, '.cai a')
    for link in cai_links:
        print(link.text)  # Just to verify the links are present
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Verify email links
    verify_email_links(driver)
    driver.save_screenshot(f'{dir}/_images/after_email_links.png')
    
    # Verify games links
    verify_games_links(driver)
    driver.save_screenshot(f'{dir}/_images/after_games_links.png')
    
    # Verify bo links
    verify_bo_links(driver)
    driver.save_screenshot(f'{dir}/_images/after_bo_links.png')
    
    # Verify cai links
    verify_cai_links(driver)
    driver.save_screenshot(f'{dir}/_images/after_cai_links.png')
