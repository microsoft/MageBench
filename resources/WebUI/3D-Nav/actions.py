
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_toggle_button(driver):
    toggle_button = driver.find_element(By.CLASS_NAME, 'toggle-btn')
    toggle_button.click()
    time.sleep(1)  # Wait for the animation to complete

def click_home_link(driver):
    home_link = driver.find_element(By.XPATH, "//li[text()='Home']")
    home_link.click()
    time.sleep(1)  # Wait for the animation to complete

def click_project_link(driver):
    project_link = driver.find_element(By.XPATH, "//li[text()='Project']")
    project_link.click()
    time.sleep(1)  # Wait for the animation to complete

def click_about_link(driver):
    about_link = driver.find_element(By.XPATH, "//li[text()='About']")
    about_link.click()
    time.sleep(1)  # Wait for the animation to complete


actions = [click_toggle_button, click_home_link, click_project_link, click_about_link]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click toggle button to show the navigation menu
    click_toggle_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle.png')
    
    # Click on Home link
    click_home_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_home_click.png')
    
    # Click on Project link
    click_project_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_project_click.png')
    
    # Click on About link
    click_about_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_about_click.png')
