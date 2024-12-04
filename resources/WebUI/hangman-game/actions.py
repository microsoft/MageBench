
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def press_letter(driver, letter):
    actions = ActionChains(driver)
    actions.send_keys(letter)
    actions.perform()
    time.sleep(1)  # Wait for the letter to be processed

def press_lettera(driver):
    actions = ActionChains(driver)
    actions.send_keys('a')
    actions.perform()
    time.sleep(1)  # Wait for the letter to be processed

def press_letterz(driver):
    actions = ActionChains(driver)
    actions.send_keys('z')
    actions.perform()
    time.sleep(1)  # Wait for the letter to be processed

def click_play_again(driver):
    play_again_button = driver.find_element(By.ID, 'play-button')
    play_again_button.click()
    time.sleep(1)  # Wait for the game to reset

actions = [press_lettera, press_letterz, press_lettera]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Press a correct letter
    press_letter(driver, 'a')
    driver.save_screenshot(f'{dir}/_images/after_correct_letter.png')
    
    # Press an incorrect letter
    press_letter(driver, 'z')
    driver.save_screenshot(f'{dir}/_images/after_incorrect_letter.png')
    
    # Press a duplicate letter
    press_letter(driver, 'a')
    driver.save_screenshot(f'{dir}/_images/after_duplicate_letter.png')
    
    # Complete the word to win the game
    for letter in 'pplication':
        press_letter(driver, letter)
    driver.save_screenshot(f'{dir}/_images/after_win.png')
    
    # Click the "Play Again" button
    click_play_again(driver)
    driver.save_screenshot(f'{dir}/_images/after_play_again.png')
