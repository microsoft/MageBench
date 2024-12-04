
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def toggle_theme(driver):
    theme_button = driver.find_element(By.CLASS_NAME, 'themer')
    theme_button.click()
    time.sleep(2)  # wait for theme transition

def follow_unfollow_first_profile(driver):
    first_follow_button = driver.find_elements(By.CLASS_NAME, 'follow-button')[0]
    first_follow_button.click()
    time.sleep(2)  # wait for follow/unfollow action

def follow_unfollow_second_profile(driver):
    second_follow_button = driver.find_elements(By.CLASS_NAME, 'follow-button')[1]
    second_follow_button.click()
    time.sleep(2)  # wait for follow/unfollow action

def follow_unfollow_third_profile(driver):
    third_follow_button = driver.find_elements(By.CLASS_NAME, 'follow-button')[2]
    third_follow_button.click()
    time.sleep(2)  # wait for follow/unfollow action

def hover_over_first_profile(driver):
    first_profile = driver.find_elements(By.CLASS_NAME, 'profile')[0]
    actions = ActionChains(driver)
    actions.move_to_element(first_profile).perform()
    time.sleep(2)  # wait for hover effect

actions = [follow_unfollow_first_profile, follow_unfollow_second_profile, follow_unfollow_third_profile]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Toggle theme
    toggle_theme(driver)
    driver.save_screenshot(f'{dir}/_images/after_toggle_theme.png')
    
    # Follow/Unfollow first profile
    follow_unfollow_first_profile(driver)
    driver.save_screenshot(f'{dir}/_images/after_follow_unfollow_first.png')
    
    # Follow/Unfollow second profile
    follow_unfollow_second_profile(driver)
    driver.save_screenshot(f'{dir}/_images/after_follow_unfollow_second.png')
    
    # Follow/Unfollow third profile
    follow_unfollow_third_profile(driver)
    driver.save_screenshot(f'{dir}/_images/after_follow_unfollow_third.png')
    
    # Hover over first profile
    hover_over_first_profile(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_first_profile.png')
