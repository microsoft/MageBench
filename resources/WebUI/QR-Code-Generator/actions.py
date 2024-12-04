
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def enter_text(driver):
    text_input = driver.find_element(By.ID, 'qr-text')
    text_input.send_keys('https://example.com')
    time.sleep(1)

def select_size(driver):
    size_dropdown = driver.find_element(By.ID, 'sizes')
    size_dropdown.click()
    time.sleep(1)
    option = driver.find_element(By.XPATH, "//option[@value='300']")
    option.click()
    time.sleep(1)

def click_generate(driver):
    generate_button = driver.find_element(By.ID, 'generateBtn')
    generate_button.click()
    time.sleep(2)  # Wait for QR code to generate

def click_download(driver):
    download_button = driver.find_element(By.ID, 'downloadBtn')
    download_button.click()
    time.sleep(1)

actions = [enter_text, select_size, click_generate]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Enter text
    enter_text(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_text.png')
    # Select size
    select_size(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_size.png')
    # Click generate
    click_generate(driver)
    driver.save_screenshot(f'{dir}/_images/after_generate.png')
    # Click download
    click_download(driver)
    driver.save_screenshot(f'{dir}/_images/after_download.png')
