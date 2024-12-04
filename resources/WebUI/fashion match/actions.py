
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_nav_item(driver, item_text):
    nav_item = driver.find_element(By.LINK_TEXT, item_text)
    nav_item.click()
    time.sleep(2)

def hover_nav_item(driver, item_text):
    nav_item = driver.find_element(By.LINK_TEXT, item_text)
    actions = ActionChains(driver)
    actions.move_to_element(nav_item).perform()
    time.sleep(2)

def click_fashion_category(driver, category_text):
    category_item = driver.find_element(By.LINK_TEXT, category_text)
    category_item.click()
    time.sleep(2)

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click on "穿搭速递" in the navigation bar
    click_nav_item(driver, '穿搭速递')
    driver.save_screenshot(f'{dir}/_images/after_click_nav.png')
    
    # Hover over "时尚大片" in the navigation bar
    hover_nav_item(driver, '时尚大片')
    driver.save_screenshot(f'{dir}/_images/after_hover_nav.png')
    
    # Click on "明星风尚" in the fashion categories
    click_fashion_category(driver, '明星风尚')
    driver.save_screenshot(f'{dir}/_images/after_click_category.png')
