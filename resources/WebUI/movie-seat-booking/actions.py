
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def select_movie(driver):
    movie_dropdown = driver.find_element(By.ID, 'movie')
    movie_dropdown.click()
    time.sleep(1)
    movie_option = driver.find_element(By.XPATH, "//option[@value='12']")
    movie_option.click()
    time.sleep(1)

def select_seat(driver):
    seat = driver.find_element(By.CSS_SELECTOR, '.row .seat:not(.occupied)')
    seat.click()
    time.sleep(1)

def deselect_seat(driver):
    seat = driver.find_element(By.CSS_SELECTOR, '.row .seat.selected')
    seat.click()
    time.sleep(1)

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Select a movie
    select_movie(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_movie.png')
    
    # Select a seat
    select_seat(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_seat.png')
    
    # Deselect the seat
    deselect_seat(driver)
    driver.save_screenshot(f'{dir}/_images/after_deselect_seat.png')

actions = [select_movie, select_seat, deselect_seat]
