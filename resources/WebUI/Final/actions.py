
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_signup_button(driver):
    signup_button = driver.find_element(By.CLASS_NAME, 'signup-btn')
    signup_button.click()
    time.sleep(2)  # wait for the modal to appear

def close_signup_modal(driver):
    signup_close_button = driver.find_element(By.CLASS_NAME, 'signup-x')
    signup_close_button.click()
    time.sleep(2)  # wait for the modal to disappear

def click_login_button(driver):
    login_button = driver.find_element(By.CLASS_NAME, 'login-btn')
    login_button.click()
    time.sleep(2)  # wait for the modal to appear

def close_login_modal(driver):
    login_close_button = driver.find_element(By.CLASS_NAME, 'login-x')
    login_close_button.click()
    time.sleep(2)  # wait for the modal to disappear

actions = [click_signup_button, close_signup_modal, click_login_button]

def interact(driver, dir):
    # save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 

    # click signup button
    click_signup_button(driver)
    # save after signup modal appears
    driver.save_screenshot(f'{dir}/_images/after_signup_click.png') 

    # close signup modal
    close_signup_modal(driver)
    # save after signup modal closes
    driver.save_screenshot(f'{dir}/_images/after_signup_close.png') 

    # click login button
    click_login_button(driver)
    # save after login modal appears
    driver.save_screenshot(f'{dir}/_images/after_login_click.png') 

    # close login modal
    close_login_modal(driver)
    # save after login modal closes
    driver.save_screenshot(f'{dir}/_images/after_login_close.png') 
