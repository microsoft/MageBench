
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_next_banner(driver):
    next_button = driver.find_element(By.CLASS_NAME, 'button-next')
    next_button.click()
    time.sleep(2)

def click_prev_banner(driver):
    prev_button = driver.find_element(By.CLASS_NAME, 'button-prev')
    prev_button.click()
    time.sleep(2)

def hover_side_menu_item(driver):
    side_menu_item = driver.find_element(By.CSS_SELECTOR, '.side-menu-item:nth-child(2) a')
    actions = ActionChains(driver)
    actions.move_to_element(side_menu_item).perform()
    time.sleep(2)

def use_search_bar(driver):
    search_input = driver.find_element(By.CSS_SELECTOR, '.search input')
    search_input.send_keys('手机')
    search_button = driver.find_element(By.CSS_SELECTOR, '.search span')
    search_button.click()
    time.sleep(2)

actions = [scroll_page, hover_side_menu_item]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click next banner button
    click_next_banner(driver)
    driver.save_screenshot(f'{dir}/_images/after_next_banner.png')
    
    # Click previous banner button
    click_prev_banner(driver)
    driver.save_screenshot(f'{dir}/_images/after_prev_banner.png')
    
    # Hover over side menu item
    hover_side_menu_item(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_side_menu.png')
    
    # Use search bar
    use_search_bar(driver)
    driver.save_screenshot(f'{dir}/_images/after_search.png')
