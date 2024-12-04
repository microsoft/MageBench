
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_navbar_link(driver):
    element = driver.find_element(By.LINK_TEXT, '餐厅')
    element.click()
    time.sleep(2)

def enter_search_text(driver):
    search_input = driver.find_element(By.ID, 'name')
    search_input.send_keys('Test Restaurant')
    time.sleep(1)

def select_city(driver):
    city_dropdown = driver.find_element(By.NAME, 'city')
    for option in city_dropdown.find_elements(By.TAG_NAME, 'option'):
        if option.text == '上海':
            option.click()
            break
    time.sleep(1)

def click_search_button(driver):
    search_button = driver.find_element(By.CLASS_NAME, 'btn-success')
    search_button.click()
    time.sleep(2)

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click on the navbar link
    click_navbar_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_navbar.png')
    
    # Enter text in the search input
    enter_search_text(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_search_text.png')
    
    # Select a city from the dropdown
    select_city(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_city.png')
    
    # Click the search button
    click_search_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_search_button.png')
