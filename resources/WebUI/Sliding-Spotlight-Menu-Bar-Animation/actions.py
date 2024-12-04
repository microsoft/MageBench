
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_home_icon(driver):
    home_icon = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(1) a')
    home_icon.click()
    time.sleep(1)

def click_bookmark_icon(driver):
    bookmark_icon = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(2) a')
    bookmark_icon.click()
    time.sleep(1)

def click_add_icon(driver):
    add_icon = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(3) a')
    add_icon.click()
    time.sleep(1)

def click_user_icon(driver):
    user_icon = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(4) a')
    user_icon.click()
    time.sleep(1)

def click_cart_icon(driver):
    cart_icon = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(5) a')
    cart_icon.click()
    time.sleep(1)

actions = [click_bookmark_icon, click_add_icon]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click home icon
    click_home_icon(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_home.png')
    
    # Click bookmark icon
    click_bookmark_icon(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_bookmark.png')
    
    # Click add icon
    click_add_icon(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_add.png')
    
    # Click user icon
    click_user_icon(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_user.png')
    
    # Click cart icon
    click_cart_icon(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_cart.png')
