
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_tab_1(driver):
    tab = driver.find_element(By.CSS_SELECTOR, '.tab-nav ul li a[data-id="1"]')
    tab.click()
    time.sleep(1)

def click_tab_2(driver):
    tab = driver.find_element(By.CSS_SELECTOR, '.tab-nav ul li a[data-id="2"]')
    tab.click()
    time.sleep(1)

def click_tab_3(driver):
    tab = driver.find_element(By.CSS_SELECTOR, '.tab-nav ul li a[data-id="3"]')
    tab.click()
    time.sleep(1)

def click_tab_4(driver):
    tab = driver.find_element(By.CSS_SELECTOR, '.tab-nav ul li a[data-id="4"]')
    tab.click()
    time.sleep(1)

actions = [click_tab_1, click_tab_2, click_tab_3, click_tab_4]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    
    # Click on each tab and save the screenshot after each click
    click_tab_1(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_tab_1.png') 
    
    click_tab_2(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_tab_2.png') 
    
    click_tab_3(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_tab_3.png') 
    
    click_tab_4(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_tab_4.png')
