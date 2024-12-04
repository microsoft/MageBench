
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_homepage(driver):
    element = driver.find_element(By.LINK_TEXT, '网站首页')
    element.click()
    time.sleep(2)

def click_about_us(driver):
    element = driver.find_element(By.LINK_TEXT, '关于我们')
    element.click()
    time.sleep(2)

def click_photography_works(driver):
    element = driver.find_element(By.LINK_TEXT, '摄影作品')
    element.click()
    time.sleep(2)

def click_contact_us(driver):
    element = driver.find_element(By.LINK_TEXT, '联系我们')
    element.click()
    time.sleep(2)

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click on homepage link
    click_homepage(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_homepage.png')
    
    # Click on about us link
    click_about_us(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_about_us.png')
    
    # Click on photography works link
    click_photography_works(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_photography_works.png')
    
    # Click on contact us link
    click_contact_us(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_contact_us.png')
