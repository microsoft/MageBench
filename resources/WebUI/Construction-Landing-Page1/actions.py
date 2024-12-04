
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

def hover_on_image_one(driver):
    image_one = driver.find_element(By.CLASS_NAME, 'img-one')
    actions = ActionChains(driver)
    actions.move_to_element(image_one).perform()
    time.sleep(1)

def hover_on_image_two(driver):
    image_two = driver.find_element(By.CLASS_NAME, 'img-two')
    actions = ActionChains(driver)
    actions.move_to_element(image_two).perform()
    time.sleep(1)

def hover_on_image_three(driver):
    image_three = driver.find_element(By.CLASS_NAME, 'img-three')
    actions = ActionChains(driver)
    actions.move_to_element(image_three).perform()
    time.sleep(1)

def fill_form(driver):
    name_input = driver.find_element(By.XPATH, "//input[@type='text']")
    email_input = driver.find_element(By.XPATH, "//input[@type='email']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    name_input.send_keys("John Doe")
    email_input.send_keys("john.doe@example.com")
    password_input.send_keys("password123")
    time.sleep(1)

actions = [scroll_page, hover_on_image_one, hover_on_image_two, hover_on_image_three, fill_form]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Hover on images
    hover_on_image_one(driver)
    driver.save_screenshot(f'{dir}/_images/hover_image_one.png')
    
    hover_on_image_two(driver)
    driver.save_screenshot(f'{dir}/_images/hover_image_two.png')
    
    hover_on_image_three(driver)
    driver.save_screenshot(f'{dir}/_images/hover_image_three.png')
    
    # Fill the form
    fill_form(driver)
    driver.save_screenshot(f'{dir}/_images/form_filled.png')
