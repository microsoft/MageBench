
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def hover_out_of_container(driver):
    actions = ActionChains(driver)
    actions.move_by_offset(0, 0).perform()
    time.sleep(2)

def hover_over_container(driver):
    container = driver.find_element(By.CLASS_NAME, 'container')
    actions = ActionChains(driver)
    actions.move_to_element(container).perform()
    time.sleep(2)

def hover_over_clip1(driver):
    clip1 = driver.find_element(By.CLASS_NAME, 'clip1')
    actions = ActionChains(driver)
    actions.move_to_element(clip1).perform()
    time.sleep(2)

def hover_over_clip2(driver):
    clip2 = driver.find_element(By.CLASS_NAME, 'clip2')
    actions = ActionChains(driver)
    actions.move_to_element(clip2).perform()
    time.sleep(2)

def hover_over_clip3(driver):
    clip3 = driver.find_element(By.CLASS_NAME, 'clip3')
    actions = ActionChains(driver)
    actions.move_to_element(clip3).perform()
    time.sleep(2)

actions = [hover_over_clip2]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Hover over container
    hover_over_container(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_container.png')
    
    # Hover over clip1
    hover_out_of_container(driver)
    hover_over_clip1(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_clip1.png')
    
    # Hover over clip2
    hover_out_of_container(driver)
    hover_over_clip2(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_clip2.png')
    
    # Hover over clip3
    hover_out_of_container(driver)
    hover_over_clip3(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_clip3.png')
