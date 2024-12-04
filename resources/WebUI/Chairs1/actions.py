
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

def click_nav_register(driver):
    nav_register_button = driver.find_element(By.CSS_SELECTOR, 'nav .btn-fill')
    nav_register_button.click()
    time.sleep(1)

def click_header_register(driver):
    header_register_button = driver.find_elements(By.CSS_SELECTOR, 'header .btn-fill')[0]
    header_register_button.click()
    time.sleep(1)

def click_learn_more(driver):
    learn_more_button = driver.find_element(By.CSS_SELECTOR, 'header .btn-outline')
    learn_more_button.click()
    time.sleep(1)

def hover_nav_links(driver):
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    nav_links = driver.find_elements(By.CSS_SELECTOR, 'nav ul li a')
    actions = ActionChains(driver)
    for link in nav_links:
        actions.move_to_element(link).perform()
        time.sleep(1)

actions = [scroll_page, hover_nav_links]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click the register button in the navigation bar
    click_nav_register(driver)
    driver.save_screenshot(f'{dir}/_images/after_nav_register.png')
    
    # Click the register button in the header
    click_header_register(driver)
    driver.save_screenshot(f'{dir}/_images/after_header_register.png')
    
    # Click the learn more button in the header
    click_learn_more(driver)
    driver.save_screenshot(f'{dir}/_images/after_learn_more.png')
    
    # Hover over the navigation links
    hover_nav_links(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_nav_links.png')
