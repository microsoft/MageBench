
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_accordion_item_1(driver):
    item_header = driver.find_element(By.XPATH, "//div[@class='accordion-item'][1]//div[@class='accordion-item-header']")
    item_header.click()
    time.sleep(1)

def click_accordion_item_2(driver):
    item_header = driver.find_element(By.XPATH, "//div[@class='accordion-item'][2]//div[@class='accordion-item-header']")
    item_header.click()
    time.sleep(1)

def click_accordion_item_3(driver):
    item_header = driver.find_element(By.XPATH, "//div[@class='accordion-item'][3]//div[@class='accordion-item-header']")
    item_header.click()
    time.sleep(1)

def click_accordion_item_4(driver):
    item_header = driver.find_element(By.XPATH, "//div[@class='accordion-item'][4]//div[@class='accordion-item-header']")
    item_header.click()
    time.sleep(1)

actions = [click_accordion_item_2, click_accordion_item_3, click_accordion_item_4]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on the first accordion item
    click_accordion_item_1(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_item_1.png')
    
    # Click on the second accordion item
    click_accordion_item_2(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_item_2.png')
    
    # Click on the third accordion item
    click_accordion_item_3(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_item_3.png')
    
    # Click on the fourth accordion item
    click_accordion_item_4(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_item_4.png')
