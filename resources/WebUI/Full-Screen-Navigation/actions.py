
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')

def click_menu_button(driver):
    button = driver.find_element(By.CLASS_NAME, 'btn')
    for _ in range(3):  # Click multiple times to handle the bug
        button.click()
        time.sleep(1)
    time.sleep(2)

def hover_over_home_link(driver):
    home_link = driver.find_element(By.XPATH, "//li/a[text()='Home']")
    actions = ActionChains(driver)
    actions.move_to_element(home_link).perform()
    time.sleep(2)

def hover_over_products_link(driver):
    products_link = driver.find_element(By.XPATH, "//li/a[text()='Products']")
    actions = ActionChains(driver)
    actions.move_to_element(products_link).perform()
    time.sleep(2)

def hover_over_news_link(driver):
    news_link = driver.find_element(By.XPATH, "//li/a[text()='News']")
    actions = ActionChains(driver)
    actions.move_to_element(news_link).perform()
    time.sleep(2)

actions = [click_menu_button, hover_over_home_link, hover_over_products_link, hover_over_news_link]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    
    # Click the menu button
    click_menu_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_menu.png')
    
    # Hover over Home link
    hover_over_home_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_home.png')
    
    # Hover over Products link
    hover_over_products_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_products.png')
    
    # Hover over News link
    hover_over_news_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_news.png')
