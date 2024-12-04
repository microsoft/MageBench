
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_first_image(driver):
    first_image = driver.find_elements(By.CSS_SELECTOR, '.img-gallery img')[0]
    first_image.click()
    time.sleep(2)

def click_second_image(driver):
    second_image = driver.find_elements(By.CSS_SELECTOR, '.img-gallery img')[1]
    second_image.click()
    time.sleep(2)

def click_close_button(driver):
    close_button = driver.find_element(By.CSS_SELECTOR, '.imageWrapper span')
    close_button.click()
    time.sleep(2)

actions = [click_first_image, click_close_button, click_second_image]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    
    # Click the first image to open the modal
    click_first_image(driver)
    driver.save_screenshot(f'{dir}/_images/after_first_image_click.png') 
    
    # Close the modal
    click_close_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_close_first_modal.png') 
    
    # Click the second image to open the modal
    click_second_image(driver)
    driver.save_screenshot(f'{dir}/_images/after_second_image_click.png') 
    
    # Close the modal
    click_close_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_close_second_modal.png') 
