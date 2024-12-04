
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_shop_now(driver):
    shop_now_button = driver.find_element(By.CLASS_NAME, 'btn-fill')
    shop_now_button.click()
    time.sleep(2)

def click_learn_more(driver):
    learn_more_button = driver.find_element(By.XPATH, "//button[text()='Learn More']")
    learn_more_button.click()
    time.sleep(2)

def click_burger_menu(driver):
    burger_menu = driver.find_element(By.CLASS_NAME, 'burger')
    burger_menu.click()
    time.sleep(2)

def hover_over_header_image(driver):
    header_image = driver.find_element(By.CLASS_NAME, 'header-img')
    actions = ActionChains(driver)
    actions.move_to_element(header_image).perform()
    time.sleep(2)

actions = [scroll_page, click_shop_now, click_learn_more]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll to see the full content
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click "Shop Now" button
    click_shop_now(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_shop_now.png')
    
    # Click "Learn More" button
    click_learn_more(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_learn_more.png')
    
    # Click burger menu
    click_burger_menu(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_burger_menu.png')
    
    # Hover over header image
    hover_over_header_image(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_header_image.png')
