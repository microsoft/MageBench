
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

def enter_height(driver):
    height_input = driver.find_element(By.ID, 'height')
    height_input.clear()
    height_input.send_keys('170')
    time.sleep(1)

def enter_weight(driver):
    weight_input = driver.find_element(By.ID, 'weight')
    weight_input.clear()
    weight_input.send_keys('70')
    time.sleep(1)

def click_compute_bmi(driver):
    compute_button = driver.find_element(By.ID, 'btn')
    compute_button.click()
    time.sleep(1)

actions = [enter_height, enter_weight, click_compute_bmi]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    # Enter height
    enter_height(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_height.png')
    # Enter weight
    enter_weight(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_weight.png')
    # Click compute BMI
    click_compute_bmi(driver)
    driver.save_screenshot(f'{dir}/_images/after_compute_bmi.png')
