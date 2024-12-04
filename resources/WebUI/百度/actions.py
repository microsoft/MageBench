
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_news_link(driver):
    news_link = driver.find_element(By.LINK_TEXT, '新闻')
    news_link.click()
    time.sleep(2)

def click_login_link(driver):
    login_link = driver.find_element(By.LINK_TEXT, '登录')
    login_link.click()
    time.sleep(2)

def enter_search_text(driver):
    search_input = driver.find_element(By.CSS_SELECTOR, '.search input')
    search_input.send_keys('Selenium WebDriver')
    time.sleep(2)

def click_search_button(driver):
    search_button = driver.find_element(By.CSS_SELECTOR, '.search button')
    search_button.click()
    time.sleep(2)

def click_set_homepage_link(driver):
    set_homepage_link = driver.find_element(By.LINK_TEXT, '把百度设为主页')
    set_homepage_link.click()
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Click on the news link
    click_news_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_news.png')
    # Click on the login link
    click_login_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_login.png')
    # Enter text into the search bar
    enter_search_text(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_search_text.png')
    # Click the search button
    click_search_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_search.png')
    # Click on the set homepage link
    click_set_homepage_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_set_homepage.png')
