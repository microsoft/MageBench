
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_new_arrivals(driver):
    new_arrivals_button = driver.find_element(By.XPATH, "//button[text()='NEW ARRIVALS']")
    new_arrivals_button.click()
    time.sleep(2)

def click_top_rating(driver):
    top_rating_button = driver.find_element(By.XPATH, "//button[text()='TOP RATING']")
    top_rating_button.click()
    time.sleep(2)

def click_best_seller(driver):
    best_seller_button = driver.find_element(By.XPATH, "//button[text()='BEST SELLER']")
    best_seller_button.click()
    time.sleep(2)

def view_first_product(driver):
    first_product_link = driver.find_element(By.XPATH, "(//a[text()='View Product'])[1]")
    first_product_link.click()
    time.sleep(2)

actions = [scroll_page, click_new_arrivals]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll to see the full content
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click on "NEW ARRIVALS"
    click_new_arrivals(driver)
    driver.save_screenshot(f'{dir}/_images/after_new_arrivals.png')
    
    # Click on "TOP RATING"
    click_top_rating(driver)
    driver.save_screenshot(f'{dir}/_images/after_top_rating.png')
    
    # Click on "BEST SELLER"
    click_best_seller(driver)
    driver.save_screenshot(f'{dir}/_images/after_best_seller.png')
    
    # Click on the first "View Product" link
    view_first_product(driver)
    driver.save_screenshot(f'{dir}/_images/after_view_product.png')
