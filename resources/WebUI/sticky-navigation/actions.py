
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for the scroll to complete

def click_about_link(driver):
    about_link = driver.find_element(By.LINK_TEXT, 'About')
    about_link.click()
    time.sleep(2)  # wait for the click action to complete

def hover_services_link(driver):
    services_link = driver.find_element(By.LINK_TEXT, 'Services')
    actions = ActionChains(driver)
    actions.move_to_element(services_link).perform()
    time.sleep(2)  # wait for the hover action to complete

def click_contact_link(driver):
    contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
    contact_link.click()
    time.sleep(2)  # wait for the click action to complete

def hover_home_link(driver):
    home_link = driver.find_element(By.LINK_TEXT, 'Home')
    actions = ActionChains(driver)
    actions.move_to_element(home_link).perform()
    time.sleep(2)  # wait for the hover action to complete

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click on 'About' link
    click_about_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_about.png')
    
    # Hover over 'Services' link
    hover_services_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_services.png')
    
    # Click on 'Contact' link
    click_contact_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_contact.png')
    
    # Hover over 'Home' link
    hover_home_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_home.png')
