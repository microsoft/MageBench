
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_navbar_button(driver):
    button = driver.find_element(By.CLASS_NAME, 'navbar-btn')
    button.click()
    time.sleep(1)  # wait for the animation to complete

def hover_over_home_icon(driver):
    home_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link:nth-child(1) i')
    actions = ActionChains(driver)
    actions.move_to_element(home_icon).perform()
    time.sleep(1)

def hover_over_city_icon(driver):
    city_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link:nth-child(2) i')
    actions = ActionChains(driver)
    actions.move_to_element(city_icon).perform()
    time.sleep(1)

def hover_over_school_icon(driver):
    school_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link:nth-child(3) i')
    actions = ActionChains(driver)
    actions.move_to_element(school_icon).perform()
    time.sleep(1)

def hover_over_landmark_icon(driver):
    landmark_icon = driver.find_element(By.CSS_SELECTOR, '.navbar-link:nth-child(4) i')
    actions = ActionChains(driver)
    actions.move_to_element(landmark_icon).perform()
    time.sleep(1)

actions = [click_navbar_button, hover_over_home_icon, hover_over_city_icon]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click the navbar button to reveal the navbar
    click_navbar_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click.png')
    
    # Hover over each icon and save the screenshot
    hover_over_home_icon(driver)
    driver.save_screenshot(f'{dir}/_images/hover_home.png')
    
    hover_over_city_icon(driver)
    driver.save_screenshot(f'{dir}/_images/hover_city.png')
    
    hover_over_school_icon(driver)
    driver.save_screenshot(f'{dir}/_images/hover_school.png')
    
    hover_over_landmark_icon(driver)
    driver.save_screenshot(f'{dir}/_images/hover_landmark.png')
