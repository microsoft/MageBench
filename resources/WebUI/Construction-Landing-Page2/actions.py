
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

def click_nav_services(driver):
    element = driver.find_element(By.LINK_TEXT, 'Services')
    element.click()
    time.sleep(1)

def hover_service_card(driver):
    card = driver.find_element(By.CSS_SELECTOR, '.card:nth-child(1)')
    actions = ActionChains(driver)
    actions.move_to_element(card).perform()
    time.sleep(1)

def hover_why_us_list(driver):
    list_item = driver.find_element(By.CSS_SELECTOR, '.list:nth-child(1) .list-info')
    actions = ActionChains(driver)
    actions.move_to_element(list_item).perform()
    time.sleep(1)

def hover_owner_image(driver):
    owner_image = driver.find_element(By.CLASS_NAME, 'owner-image')
    actions = ActionChains(driver)
    actions.move_to_element(owner_image).perform()
    time.sleep(1)

actions = [scroll_page, click_nav_services, hover_service_card, hover_why_us_list, hover_owner_image]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click on 'Services' in the navigation
    click_nav_services(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_services.png')
    
    # Hover over the first service card
    hover_service_card(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_service_card.png')
    
    # Hover over the first 'Why Us?' list item
    hover_why_us_list(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_why_us_list.png')
    
    # Hover over the owner image
    hover_owner_image(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_owner_image.png')
