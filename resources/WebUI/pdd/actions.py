
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_homepage(driver):
    element = driver.find_element(By.XPATH, "//li[@class='pn-other-item']/span[text()='首页']")
    element.click()
    time.sleep(2)

def click_merchant_entry(driver):
    element = driver.find_element(By.XPATH, "//li[@class='pn-other-item']/span[text()='拼多多商家入驻']")
    element.click()
    time.sleep(2)

def click_cross_border_entry(driver):
    element = driver.find_element(By.XPATH, "//li[@class='pn-other-item']/span[text()='跨境商家入驻']")
    element.click()
    time.sleep(2)

def click_hot_news(driver):
    element = driver.find_element(By.XPATH, "//li[@class='pn-other-item']/span[text()='热点资讯']")
    element.click()
    time.sleep(2)

def hover_qr_code(driver):
    element_to_hover = driver.find_element(By.CLASS_NAME, 'pdd-left-code')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on '首页'
    click_homepage(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_homepage.png')
    
    # Click on '拼多多商家入驻'
    click_merchant_entry(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_merchant_entry.png')
    
    # Click on '跨境商家入驻'
    click_cross_border_entry(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_cross_border_entry.png')
    
    # Click on '热点资讯'
    click_hot_news(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_hot_news.png')
    
    # Hover over the QR code
    hover_qr_code(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_qr_code.png')
