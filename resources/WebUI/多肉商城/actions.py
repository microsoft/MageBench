
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for the scroll to complete

def hover_over_first_product(driver):
    first_product = driver.find_elements(By.CLASS_NAME, 'view')[0]
    hover = ActionChains(driver).move_to_element(first_product)
    hover.perform()
    time.sleep(2)  # wait for the hover effect to complete

def hover_over_second_product(driver):
    second_product = driver.find_elements(By.CLASS_NAME, 'view')[1]
    hover = ActionChains(driver).move_to_element(second_product)
    hover.perform()
    time.sleep(2)  # wait for the hover effect to complete

def hover_over_third_product(driver):
    third_product = driver.find_elements(By.CLASS_NAME, 'view')[2]
    hover = ActionChains(driver).move_to_element(third_product)
    hover.perform()
    time.sleep(2)  # wait for the hover effect to complete

def click_first_service_link(driver):
    first_service_link = driver.find_elements(By.CSS_SELECTOR, '.services a')[0]
    first_service_link.click()
    time.sleep(2)  # wait for the click action to complete

actions = [scroll_page, hover_over_first_product]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Hover over the first product
    hover_over_first_product(driver)
    driver.save_screenshot(f'{dir}/_images/hover_first_product.png')
    
    # Hover over the second product
    hover_over_second_product(driver)
    driver.save_screenshot(f'{dir}/_images/hover_second_product.png')
    
    # Hover over the third product
    hover_over_third_product(driver)
    driver.save_screenshot(f'{dir}/_images/hover_third_product.png')
    
    # Click the first service link
    click_first_service_link(driver)
    driver.save_screenshot(f'{dir}/_images/click_first_service_link.png')
