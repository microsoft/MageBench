
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_star_1(driver):
    star = driver.find_element(By.CSS_SELECTOR, '.fa-star:nth-child(1)')
    star.click()
    time.sleep(1)

def click_star_2(driver):
    star = driver.find_element(By.CSS_SELECTOR, '.fa-star:nth-child(2)')
    star.click()
    time.sleep(1)

def click_star_3(driver):
    star = driver.find_element(By.CSS_SELECTOR, '.fa-star:nth-child(3)')
    star.click()
    time.sleep(1)

def click_star_4(driver):
    star = driver.find_element(By.CSS_SELECTOR, '.fa-star:nth-child(4)')
    star.click()
    time.sleep(1)

def click_star_5(driver):
    star = driver.find_element(By.CSS_SELECTOR, '.fa-star:nth-child(5)')
    star.click()
    time.sleep(1)

actions = [click_star_1, click_star_2, click_star_3, click_star_4, click_star_5]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Perform actions and save screenshots
    for i, action in enumerate(actions):
        action(driver)
        driver.save_screenshot(f'{dir}/_images/after_click_star_{i+1}.png')
