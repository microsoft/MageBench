
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_hamburger_menu(driver):
    element = driver.find_element(By.CSS_SELECTOR, 'label[for="menu"]')
    element.click()
    time.sleep(2)  # Wait for the menu to animate

def hover_home_menu_item(driver):
    element_to_hover = driver.find_element(By.CSS_SELECTOR, '.menu__item:nth-child(1)')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)  # Wait for the hover animation

def hover_about_menu_item(driver):
    element_to_hover = driver.find_element(By.CSS_SELECTOR, '.menu__item:nth-child(2)')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)  # Wait for the hover animation

def hover_contact_menu_item(driver):
    element_to_hover = driver.find_element(By.CSS_SELECTOR, '.menu__item:nth-child(3)')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover).perform()
    time.sleep(2)  # Wait for the hover animation

actions = [click_hamburger_menu, hover_about_menu_item, hover_contact_menu_item]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the hamburger menu
    click_hamburger_menu(driver)
    driver.save_screenshot(f'{dir}/_images/after_click.png')
    
    # Hover over "Home" menu item
    hover_home_menu_item(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_home.png')
    
    # Hover over "About" menu item
    hover_about_menu_item(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_about.png')
    
    # Hover over "Contact" menu item
    hover_contact_menu_item(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_contact.png')
