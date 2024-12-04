
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_menu_button(driver):
    menu_button = driver.find_element(By.CLASS_NAME, 'menu-button')
    menu_button.click()
    time.sleep(1)  # Wait for the animation to complete

def hover_over_settings(driver):
    settings_item = driver.find_element(By.XPATH, "//span[text()='Settings']")
    actions = ActionChains(driver)
    actions.move_to_element(settings_item).perform()
    time.sleep(1)  # Wait for the hover effect

def hover_over_copy(driver):
    copy_item = driver.find_element(By.XPATH, "//span[text()='Copy']")
    actions = ActionChains(driver)
    actions.move_to_element(copy_item).perform()
    time.sleep(1)  # Wait for the hover effect

def hover_over_share(driver):
    share_item = driver.find_element(By.XPATH, "//span[text()='Share']")
    actions = ActionChains(driver)
    actions.move_to_element(share_item).perform()
    time.sleep(1)  # Wait for the hover effect

def hover_over_delete(driver):
    delete_item = driver.find_element(By.XPATH, "//span[text()='Delete']")
    actions = ActionChains(driver)
    actions.move_to_element(delete_item).perform()
    time.sleep(1)  # Wait for the hover effect

actions = [click_menu_button, hover_over_settings]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the menu button
    click_menu_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click.png')
    
    # Hover over each menu item and save screenshots
    hover_over_settings(driver)
    driver.save_screenshot(f'{dir}/_images/hover_settings.png')
    
    hover_over_copy(driver)
    driver.save_screenshot(f'{dir}/_images/hover_copy.png')
    
    hover_over_share(driver)
    driver.save_screenshot(f'{dir}/_images/hover_share.png')
    
    hover_over_delete(driver)
    driver.save_screenshot(f'{dir}/_images/hover_delete.png')
