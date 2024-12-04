
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_read_more(driver):
    read_more_button = driver.find_element(By.CSS_SELECTOR, '.btn')
    read_more_button.click()
    time.sleep(2)

def submit_email_form(driver):
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys('test@example.com')
    submit_button = driver.find_element(By.CSS_SELECTOR, '.submit')
    submit_button.click()
    time.sleep(2)

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click "Read More" button
    click_read_more(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_read_more.png')
    
    # Submit email form
    submit_email_form(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit_email.png')
