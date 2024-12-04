
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_nav_home(driver):
    element = driver.find_element(By.LINK_TEXT, '首页')
    element.click()
    time.sleep(2)

def click_nav_courses(driver):
    element = driver.find_element(By.LINK_TEXT, '课程')
    element.click()
    time.sleep(2)

def use_search_bar(driver):
    search_input = driver.find_element(By.CSS_SELECTOR, '.search input')
    search_input.send_keys('Python')
    search_button = driver.find_element(By.CSS_SELECTOR, '.search button')
    search_button.click()
    time.sleep(2)

def click_all_courses(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.course .more')
    element.click()
    time.sleep(2)

def click_modify_interests(driver):
    element = driver.find_element(By.CSS_SELECTOR, '.goods .mod')
    element.click()
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on "首页" (Home)
    click_nav_home(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_home.png')
    
    # Click on "课程" (Courses)
    click_nav_courses(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_courses.png')
    
    # Use the search bar
    use_search_bar(driver)
    driver.save_screenshot(f'{dir}/_images/after_search.png')
    
    # Click on "全部课程" (All Courses)
    click_all_courses(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_all_courses.png')
    
    # Click on "修改兴趣" (Modify Interests)
    click_modify_interests(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_modify_interests.png')
