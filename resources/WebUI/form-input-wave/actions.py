
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def focus_email_input(driver):
    email_input = driver.find_element(By.CSS_SELECTOR, '.form-control input[type="text"]')
    email_input.click()
    time.sleep(2)

def focus_password_input(driver):
    password_input = driver.find_element(By.CSS_SELECTOR, '.form-control input[type="password"]')
    password_input.click()
    time.sleep(2)

def click_login_button(driver):
    login_button = driver.find_element(By.CSS_SELECTOR, '.btn')
    login_button.click()
    time.sleep(2)

def click_register_link(driver):
    register_link = driver.find_element(By.CSS_SELECTOR, '.text a')
    register_link.click()
    time.sleep(2)

actions = [focus_email_input, focus_password_input, click_login_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    # Focus on email input
    focus_email_input(driver)
    driver.save_screenshot(f'{dir}/_images/focus_email.png')
    # Focus on password input
    focus_password_input(driver)
    driver.save_screenshot(f'{dir}/_images/focus_password.png')
    # Click login button
    click_login_button(driver)
    driver.save_screenshot(f'{dir}/_images/click_login.png')
    # Click register link
    click_register_link(driver)
    driver.save_screenshot(f'{dir}/_images/click_register.png')
