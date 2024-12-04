
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_on_soaring_list(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.main .box dl:nth-child(1) .top a img')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_on_new_song_list(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.main .box dl:nth-child(2) .top a img')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_on_original_list(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.main .box dl:nth-child(3) .top a img')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_on_first_song_in_soaring_list(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.main .box dl:nth-child(1) dd ol li:nth-child(1) .song a')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

def hover_on_first_anchor(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.sidebar .anchor .hotdj li:nth-child(1) a img')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Hover on soaring list
    hover_on_soaring_list(driver)
    driver.save_screenshot(f'{dir}/_images/hover_on_soaring_list.png')
    
    # Hover on new song list
    hover_on_new_song_list(driver)
    driver.save_screenshot(f'{dir}/_images/hover_on_new_song_list.png')
    
    # Hover on original list
    hover_on_original_list(driver)
    driver.save_screenshot(f'{dir}/_images/hover_on_original_list.png')
    
    # Hover on first song in soaring list
    hover_on_first_song_in_soaring_list(driver)
    driver.save_screenshot(f'{dir}/_images/hover_on_first_song_in_soaring_list.png')
    
    # Hover on first anchor
    hover_on_first_anchor(driver)
    driver.save_screenshot(f'{dir}/_images/hover_on_first_anchor.png')
