
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_hamburger_menu(driver):
    menu = driver.find_element(By.CLASS_NAME, 'menu')
    menu.click()
    time.sleep(1)  # Wait for the menu animation to complete

def close_hamburger_menu(driver):
    menu = driver.find_element(By.CLASS_NAME, 'menu')
    menu.click()
    time.sleep(1)  # Wait for the menu animation to complete

def click_slider_dot_2(driver):
    dot = driver.find_elements(By.CLASS_NAME, 'slide')[1]
    dot.click()
    time.sleep(1)  # Wait for the slide transition to complete

def click_slider_dot_3(driver):
    dot = driver.find_elements(By.CLASS_NAME, 'slide')[2]
    dot.click()
    time.sleep(1)  # Wait for the slide transition to complete

def hover_hero_image(driver):
    hero_image = driver.find_element(By.CLASS_NAME, 'hero')
    actions = ActionChains(driver)
    actions.move_to_element(hero_image).perform()
    time.sleep(1)  # Wait for the hover animation to complete

actions = [click_hamburger_menu, close_hamburger_menu, click_slider_dot_2, click_slider_dot_3, hover_hero_image]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click hamburger menu to open
    click_hamburger_menu(driver)
    driver.save_screenshot(f'{dir}/_images/menu_open.png')
    
    # Close hamburger menu
    close_hamburger_menu(driver)
    driver.save_screenshot(f'{dir}/_images/menu_closed.png')
    
    # Click on the second slider dot
    click_slider_dot_2(driver)
    driver.save_screenshot(f'{dir}/_images/slider_dot_2.png')
    
    # Click on the third slider dot
    click_slider_dot_3(driver)
    driver.save_screenshot(f'{dir}/_images/slider_dot_3.png')
    
    # Hover over the hero image
    hover_hero_image(driver)
    driver.save_screenshot(f'{dir}/_images/hover_hero.png')
