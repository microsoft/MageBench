
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def toggle_sidebar(driver):
    hamburger_menu = driver.find_element(By.CLASS_NAME, 'hamburger-menu')
    hamburger_menu.click()
    time.sleep(2)

def expand_dashboard_submenu(driver):
    dashboard_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Dashboard')]")
    dashboard_link.click()
    time.sleep(2)

def expand_ecommerce_submenu(driver):
    ecommerce_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'E-commerce')]")
    ecommerce_link.click()
    time.sleep(2)

def expand_components_submenu(driver):
    components_link = driver.find_element(By.XPATH, "//a[@class='nav-link' and contains(., 'Components')]")
    components_link.click()
    time.sleep(2)

def click_search_button(driver):
    search_button = driver.find_element(By.CLASS_NAME, 'search-button')
    search_button.click()
    time.sleep(2)

actions = [toggle_sidebar, expand_dashboard_submenu]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Toggle sidebar
    toggle_sidebar(driver)
    driver.save_screenshot(f'{dir}/_images/sidebar_toggled.png')
    
    # Expand Dashboard submenu
    expand_dashboard_submenu(driver)
    driver.save_screenshot(f'{dir}/_images/dashboard_expanded.png')
    
    # Expand E-commerce submenu
    expand_ecommerce_submenu(driver)
    driver.save_screenshot(f'{dir}/_images/ecommerce_expanded.png')
    
    # Expand Components submenu
    expand_components_submenu(driver)
    driver.save_screenshot(f'{dir}/_images/components_expanded.png')
    
    # Click search button
    click_search_button(driver)
    driver.save_screenshot(f'{dir}/_images/search_clicked.png')
