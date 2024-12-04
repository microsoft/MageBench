
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_menu_link(driver):
    menu_link = driver.find_element(By.CSS_SELECTOR, 'h1 a[href="#menu"]')
    menu_link.click()
    time.sleep(2)  # Wait for the menu to appear

def hover_home_link(driver):
    home_link = driver.find_element(By.CSS_SELECTOR, '.nav_list_item:nth-child(1) a')
    actions = ActionChains(driver)
    actions.move_to_element(home_link).perform()
    time.sleep(2)  # Wait to observe the hover effect

def hover_about_link(driver):
    about_link = driver.find_element(By.CSS_SELECTOR, '.nav_list_item:nth-child(2) a')
    actions = ActionChains(driver)
    actions.move_to_element(about_link).perform()
    time.sleep(2)  # Wait to observe the hover effect

def hover_products_link(driver):
    products_link = driver.find_element(By.CSS_SELECTOR, '.nav_list_item:nth-child(3) a')
    actions = ActionChains(driver)
    actions.move_to_element(products_link).perform()
    time.sleep(2)  # Wait to observe the hover effect

def hover_services_link(driver):
    services_link = driver.find_element(By.CSS_SELECTOR, '.nav_list_item:nth-child(4) a')
    actions = ActionChains(driver)
    actions.move_to_element(services_link).perform()
    time.sleep(2)  # Wait to observe the hover effect

actions = [click_menu_link, hover_home_link]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the menu link
    click_menu_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_menu.png')
    
    # Hover over each menu item and save screenshots
    hover_home_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_home.png')
    
    hover_about_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_about.png')
    
    hover_products_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_products.png')
    
    hover_services_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_services.png')
