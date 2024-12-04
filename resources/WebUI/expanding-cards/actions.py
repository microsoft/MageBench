
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_first_panel(driver):
    first_panel = driver.find_element(By.CSS_SELECTOR, '.panel:nth-child(1)')
    first_panel.click()
    time.sleep(1)

def click_second_panel(driver):
    second_panel = driver.find_element(By.CSS_SELECTOR, '.panel:nth-child(2)')
    second_panel.click()
    time.sleep(1)

def click_third_panel(driver):
    third_panel = driver.find_element(By.CSS_SELECTOR, '.panel:nth-child(3)')
    third_panel.click()
    time.sleep(1)

def click_fourth_panel(driver):
    fourth_panel = driver.find_element(By.CSS_SELECTOR, '.panel:nth-child(4)')
    fourth_panel.click()
    time.sleep(1)

def click_fifth_panel(driver):
    fifth_panel = driver.find_element(By.CSS_SELECTOR, '.panel:nth-child(5)')
    fifth_panel.click()
    time.sleep(1)

actions = [click_second_panel, click_third_panel, click_fourth_panel, click_fifth_panel]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 

    # Click on each panel and save the screenshot after each click
    click_first_panel(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_first_panel.png') 

    click_second_panel(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_second_panel.png') 

    click_third_panel(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_third_panel.png') 

    click_fourth_panel(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_fourth_panel.png') 

    click_fifth_panel(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_fifth_panel.png') 
