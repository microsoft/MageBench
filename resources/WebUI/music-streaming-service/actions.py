
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_discover_link(driver):
    discover_link = driver.find_element(By.LINK_TEXT, 'Discover')
    discover_link.click()
    time.sleep(2)

def click_join_link(driver):
    join_link = driver.find_element(By.LINK_TEXT, 'Join')
    join_link.click()
    time.sleep(2)

def click_join_now_button(driver):
    join_now_button = driver.find_element(By.CSS_SELECTOR, '.hero-section .btn')
    join_now_button.click()
    time.sleep(2)

def fill_and_submit_form(driver):
    name_input = driver.find_element(By.CSS_SELECTOR, '.join-form input[type="text"]')
    email_input = driver.find_element(By.CSS_SELECTOR, '.join-form input[type="email"]')
    password_input = driver.find_element(By.CSS_SELECTOR, '.join-form input[type="password"]')
    submit_button = driver.find_element(By.CSS_SELECTOR, '.join-form button[type="submit"]')
    
    name_input.send_keys("Test User")
    email_input.send_keys("test@example.com")
    password_input.send_keys("password123")
    submit_button.click()
    time.sleep(2)

actions = [scroll_page, click_discover_link]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click "Discover" link
    click_discover_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_discover.png')
    
    # Click "Join" link
    click_join_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_join.png')
    
    # Click "Join Now" button
    click_join_now_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_join_now.png')
    
    # Fill and submit the form
    fill_and_submit_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_form_submission.png')
