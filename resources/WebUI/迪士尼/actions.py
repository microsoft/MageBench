
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def hover_on_first_castle(driver):
    first_castle = driver.find_element(By.CSS_SELECTOR, '.content-row')
    actions = ActionChains(driver)
    actions.move_to_element(first_castle).perform()
    time.sleep(2)

def hover_on_second_castle(driver):
    second_castle = driver.find_element(By.CSS_SELECTOR, '.content-row:nth-child(2)')
    actions = ActionChains(driver)
    actions.move_to_element(second_castle).perform()
    time.sleep(2)

def hover_on_third_castle(driver):
    third_castle = driver.find_element(By.CSS_SELECTOR, '.content-row:nth-child(3)')
    actions = ActionChains(driver)
    actions.move_to_element(third_castle).perform()
    time.sleep(2)

def hover_on_fourth_castle(driver):
    fourth_castle = driver.find_element(By.CSS_SELECTOR, '.content-row:nth-child(4)')
    actions = ActionChains(driver)
    actions.move_to_element(fourth_castle).perform()
    time.sleep(2)

actions = [scroll_page, hover_on_first_castle, hover_on_second_castle, hover_on_third_castle, hover_on_fourth_castle]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Hover over the first castle
    hover_on_first_castle(driver)
    driver.save_screenshot(f'{dir}/_images/hover_first_castle.png')
    
    # Hover over the second castle
    hover_on_second_castle(driver)
    driver.save_screenshot(f'{dir}/_images/hover_second_castle.png')
    
    # Hover over the third castle
    hover_on_third_castle(driver)
    driver.save_screenshot(f'{dir}/_images/hover_third_castle.png')
    
    # Hover over the fourth castle
    hover_on_fourth_castle(driver)
    driver.save_screenshot(f'{dir}/_images/hover_fourth_castle.png')
