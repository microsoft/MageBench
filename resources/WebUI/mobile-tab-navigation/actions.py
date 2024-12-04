
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_home_tab(driver):
    home_tab = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(1)')
    home_tab.click()
    time.sleep(2)

def click_work_tab(driver):
    work_tab = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(2)')
    work_tab.click()
    time.sleep(2)

def click_blog_tab(driver):
    blog_tab = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(3)')
    blog_tab.click()
    time.sleep(2)

def click_about_tab(driver):
    about_tab = driver.find_element(By.CSS_SELECTOR, 'nav ul li:nth-child(4)')
    about_tab.click()
    time.sleep(2)

actions = [click_work_tab, click_blog_tab, click_about_tab]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png') 
    
    # Click Home tab
    click_home_tab(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_home.png') 
    
    # Click Work tab
    click_work_tab(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_work.png') 
    
    # Click Blog tab
    click_blog_tab(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_blog.png') 
    
    # Click About Us tab
    click_about_tab(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_about.png') 
