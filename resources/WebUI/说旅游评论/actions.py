
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_home(driver):
    home_link = driver.find_element(By.XPATH, "//p[contains(text(), '旅游首页')]")
    home_link.click()
    time.sleep(2)

def click_login(driver):
    login_link = driver.find_element(By.XPATH, "//p[contains(text(), '登录')]")
    login_link.click()
    time.sleep(2)

def click_register(driver):
    register_link = driver.find_element(By.XPATH, "//p[contains(text(), '注册')]")
    register_link.click()
    time.sleep(2)

def hover_logo(driver):
    logo = driver.find_element(By.XPATH, "//img[@src='images/logo.png']")
    actions = ActionChains(driver)
    actions.move_to_element(logo).perform()
    time.sleep(2)

def hover_banner(driver):
    banner = driver.find_element(By.XPATH, "//img[@src='images/banner2.jpg']")
    actions = ActionChains(driver)
    actions.move_to_element(banner).perform()
    time.sleep(2)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click on Home
    click_home(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_home.png')
    
    # Click on Login
    click_login(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_login.png')
    
    # Click on Register
    click_register(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_register.png')
    
    # Hover over the logo
    hover_logo(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_logo.png')
    
    # Hover over the banner
    hover_banner(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_banner.png')
