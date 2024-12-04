
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_state(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def click_get_another_joke(driver):
    joke_button = driver.find_element(By.ID, 'jokeBtn')
    joke_button.click()
    time.sleep(2)  # Wait for the joke to be fetched and displayed

actions = [click_get_another_joke]

def interact(driver, dir):
    # Save the initial state of the webpage
    save_initial_state(driver, dir)
    
    # Click the "Get Another Joke" button and save the state after the joke is fetched
    click_get_another_joke(driver)
    driver.save_screenshot(f'{dir}/_images/after_click.png')
