
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

def filter_posts(driver):
    filter_input = driver.find_element(By.ID, 'filter')
    filter_input.send_keys('qui')
    time.sleep(2)  # Wait for the filtering to take effect

def scroll_to_load_more_posts(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for new posts to load

actions = [filter_posts, scroll_to_load_more_posts]

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
    
    # Filter posts
    filter_posts(driver)
    driver.save_screenshot(f'{dir}/_images/after_filter.png')
    
    # Scroll to load more posts
    scroll_to_load_more_posts(driver)
    driver.save_screenshot(f'{dir}/_images/after_scroll.png')
