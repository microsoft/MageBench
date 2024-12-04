
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_select_program_header(driver):
    element = driver.find_element(By.LINK_TEXT, 'Select Program')
    element.click()
    time.sleep(2)

def click_view_menu_header(driver):
    element = driver.find_element(By.LINK_TEXT, 'View Menu')
    element.click()
    time.sleep(2)

def click_select_program_delivery(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.delivery .main-btn-fill')
    element.click()
    time.sleep(2)

def click_view_menu_delivery(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.delivery .main-btn')
    element.click()
    time.sleep(2)

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click "Select Program" in the header
    click_select_program_header(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_select_program_header.png')
    
    # Click "View Menu" in the header
    click_view_menu_header(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_view_menu_header.png')
    
    # Click "Select Program" in the delivery section
    click_select_program_delivery(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_select_program_delivery.png')
    
    # Click "View Menu" in the delivery section
    click_view_menu_delivery(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_view_menu_delivery.png')
