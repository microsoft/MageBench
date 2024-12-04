
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

def click_shop_now(driver):
    shop_now_button = driver.find_element(By.CLASS_NAME, 'main-btn')
    shop_now_button.click()
    time.sleep(1)

def click_learn_more(driver):
    learn_more_button = driver.find_element(By.XPATH, "//section[@id='our-story']//button[text()='Learn More']")
    learn_more_button.click()
    time.sleep(1)

def hover_nav_links(driver):
    nav_links = driver.find_elements(By.CSS_SELECTOR, 'nav ul li a')
    actions = ActionChains(driver)
    for link in nav_links:
        actions.move_to_element(link).perform()
        time.sleep(1)

actions = [scroll_page, click_shop_now, hover_nav_links]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click "Shop Now" button
    click_shop_now(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_shop_now.png')
    
    # Click "Learn More" button
    click_learn_more(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_learn_more.png')
    
    # Hover over navigation links
    hover_nav_links(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_nav_links.png')
