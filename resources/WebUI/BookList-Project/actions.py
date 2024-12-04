
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def fill_title(driver):
    title_input = driver.find_element(By.ID, 'title')
    title_input.send_keys('The Great Gatsby')
    time.sleep(1)

def fill_author(driver):
    author_input = driver.find_element(By.ID, 'author')
    author_input.send_keys('F. Scott Fitzgerald')
    time.sleep(1)

def fill_year(driver):
    year_input = driver.find_element(By.ID, 'year')
    year_input.send_keys('1925')
    time.sleep(1)

def click_add_book(driver):
    add_button = driver.find_element(By.CLASS_NAME, 'btn')
    add_button.click()
    time.sleep(1)

def save_final_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/final.png')

actions = [fill_title, fill_author, fill_year, click_add_book]

def interact(driver, dir):
    save_initial_screenshot(driver, dir)
    fill_title(driver)
    fill_author(driver)
    fill_year(driver)
    click_add_book(driver)
    save_final_screenshot(driver, dir)
