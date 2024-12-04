
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_navigation_link(driver):
    nav_link = driver.find_element(By.XPATH, "//ul[@class='nav Float no14']/li[1]/a")
    nav_link.click()
    time.sleep(2)

def use_search_bar(driver):
    search_input = driver.find_element(By.XPATH, "//div[@class='Search Float']/input")
    search_input.send_keys("test search")
    time.sleep(2)

def click_play_button(driver):
    play_button = driver.find_element(By.XPATH, "//ul/li[1]//a[@class='icon-play']")
    play_button.click()
    time.sleep(2)

def click_login_sidebar(driver):
    login_link = driver.find_element(By.XPATH, "//div[@class='sidebar sidebar-w Float Border']//a[text()='用户登录']")
    login_link.click()
    time.sleep(2)

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png') 
    # Click navigation link
    click_navigation_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_navigation.png') 
    # Use search bar
    use_search_bar(driver)
    driver.save_screenshot(f'{dir}/_images/after_search.png') 
    # Click play button
    click_play_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_play.png') 
    # Click login link in sidebar
    click_login_sidebar(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_login.png') 
