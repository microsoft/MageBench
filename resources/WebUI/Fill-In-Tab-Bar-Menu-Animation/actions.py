
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_tab_1(driver):
    tab_1 = driver.find_element(By.CSS_SELECTOR, 'label[for="tab-01"] svg')
    tab_1.click()
    time.sleep(2)

def click_tab_2(driver):
    tab_2 = driver.find_element(By.CSS_SELECTOR, 'label[for="tab-02"] svg')
    tab_2.click()
    time.sleep(2)

def click_tab_3(driver):
    tab_3 = driver.find_element(By.CSS_SELECTOR, 'label[for="tab-03"] svg')
    tab_3.click()
    time.sleep(2)

def click_tab_4(driver):
    tab_4 = driver.find_element(By.CSS_SELECTOR, 'label[for="tab-04"] svg')
    tab_4.click()
    time.sleep(2)

actions = [click_tab_2, click_tab_3, click_tab_4]

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
