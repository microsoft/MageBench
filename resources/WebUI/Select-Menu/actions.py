
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_select_field(driver):
    select_field = driver.find_element(By.ID, 'selectField')
    select_field.click()
    time.sleep(1)  # wait for the dropdown to appear

def select_facebook(driver):
    facebook_option = driver.find_elements(By.CLASS_NAME, 'options')[0]
    facebook_option.click()
    time.sleep(1)  # wait for the selection to be reflected

def select_instagram(driver):
    select_field = driver.find_element(By.ID, 'selectField')
    select_field.click()
    time.sleep(1)  # wait for the dropdown to appear
    instagram_option = driver.find_elements(By.CLASS_NAME, 'options')[1]
    instagram_option.click()
    time.sleep(1)  # wait for the selection to be reflected

def select_twitter(driver):
    select_field = driver.find_element(By.ID, 'selectField')
    select_field.click()
    time.sleep(1)  # wait for the dropdown to appear
    twitter_option = driver.find_elements(By.CLASS_NAME, 'options')[3]
    twitter_option.click()
    time.sleep(1)  # wait for the selection to be reflected

def select_youtube(driver):
    select_field = driver.find_element(By.ID, 'selectField')
    select_field.click()
    time.sleep(1)  # wait for the dropdown to appear
    youtube_option = driver.find_elements(By.CLASS_NAME, 'options')[5]
    youtube_option.click()
    time.sleep(1)  # wait for the selection to be reflected

actions = [click_select_field]

def interact(driver, dir):
    # save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 

    # click to open dropdown
    click_select_field(driver)
    driver.save_screenshot(f'{dir}/_images/dropdown_open.png') 

    # select Facebook
    select_facebook(driver)
    driver.save_screenshot(f'{dir}/_images/facebook_selected.png') 

    # select Instagram
    select_instagram(driver)
    driver.save_screenshot(f'{dir}/_images/instagram_selected.png') 

    # select Twitter
    select_twitter(driver)
    driver.save_screenshot(f'{dir}/_images/twitter_selected.png') 

    # select YouTube
    select_youtube(driver)
    driver.save_screenshot(f'{dir}/_images/youtube_selected.png') 
