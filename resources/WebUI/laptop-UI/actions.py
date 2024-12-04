
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_14_inch_button(driver):
    button = driver.find_element(By.CLASS_NAME, 'cta-select')
    button.click()
    time.sleep(2)

def click_add_to_cart_button(driver):
    button = driver.find_element(By.CLASS_NAME, 'cta-add')
    button.click()
    time.sleep(2)

def hover_over_nav_links(driver):
    nav_links = driver.find_elements(By.CLASS_NAME, 'nav-link')
    actions = ActionChains(driver)
    for link in nav_links:
        actions.move_to_element(link).perform()
        time.sleep(1)

def click_nav_link(driver):
    link = driver.find_element(By.LINK_TEXT, 'Products')
    link.click()
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    # Click the 14 Inch button
    click_14_inch_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_14_inch.png') 
    # Click the Add to Cart button
    click_add_to_cart_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_add_to_cart.png') 
    # Hover over navigation links
    hover_over_nav_links(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_nav_links.png') 
    # Click the Products navigation link
    click_nav_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_nav_link.png') 
