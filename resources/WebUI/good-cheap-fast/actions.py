
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_good(driver):
    good_label = driver.find_element(By.CSS_SELECTOR, 'label[for="good"]')
    good_label.click()
    time.sleep(1)

def click_cheap(driver):
    cheap_label = driver.find_element(By.CSS_SELECTOR, 'label[for="cheap"]')
    cheap_label.click()
    time.sleep(1)

def click_fast(driver):
    fast_label = driver.find_element(By.CSS_SELECTOR, 'label[for="fast"]')
    fast_label.click()
    time.sleep(1)

actions = [click_good, click_cheap, click_fast]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on "Good"
    click_good(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_good.png')
    
    # Click on "Cheap"
    click_cheap(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_cheap.png')
    
    # Click on "Fast"
    click_fast(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_fast.png')
    
    # Click on "Good" again to see the toggle logic in action
    click_good(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_good_again.png')
