
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_add_new_card(driver):
    add_new_card_button = driver.find_element(By.ID, 'show')
    add_new_card_button.click()
    time.sleep(1)

def add_card(driver):
    question_input = driver.find_element(By.ID, 'question')
    answer_input = driver.find_element(By.ID, 'answer')
    add_card_button = driver.find_element(By.ID, 'add-card')
    
    question_input.send_keys("What is the capital of France?")
    answer_input.send_keys("Paris")
    add_card_button.click()
    time.sleep(1)

def navigate_next(driver):
    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(1)

def navigate_prev(driver):
    prev_button = driver.find_element(By.ID, 'prev')
    prev_button.click()
    time.sleep(1)

def clear_cards(driver):
    clear_button = driver.find_element(By.ID, 'clear')
    clear_button.click()
    time.sleep(1)

actions = [click_add_new_card, add_card, navigate_next, navigate_prev, clear_cards]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click to add new card
    click_add_new_card(driver)
    driver.save_screenshot(f'{dir}/_images/add_new_card_form.png')
    
    # Add a card
    add_card(driver)
    driver.save_screenshot(f'{dir}/_images/card_added.png')
    
    # Navigate to next card
    navigate_next(driver)
    driver.save_screenshot(f'{dir}/_images/navigate_next.png')
    
    # Navigate to previous card
    navigate_prev(driver)
    driver.save_screenshot(f'{dir}/_images/navigate_prev.png')
    
    # Clear all cards
    clear_cards(driver)
    driver.save_screenshot(f'{dir}/_images/clear_cards.png')
