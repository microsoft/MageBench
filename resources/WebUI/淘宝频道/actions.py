
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_ad_link(driver):
    ad_link = driver.find_element(By.XPATH, "//div[@class='ad']/a[1]")
    ad_link.click()
    time.sleep(2)

def hover_first_product(driver):
    first_product = driver.find_element(By.XPATH, "//ul/li[1]")
    actions = ActionChains(driver)
    actions.move_to_element(first_product).perform()
    time.sleep(2)

def click_first_product_image(driver):
    first_product_image = driver.find_element(By.XPATH, "//ul/li[1]/a/img")
    first_product_image.click()
    time.sleep(2)

def click_first_product_comment(driver):
    first_product_comment = driver.find_element(By.XPATH, "//ul/li[1]//a[@class='comment']")
    first_product_comment.click()
    time.sleep(2)

def click_first_product_price(driver):
    first_product_price = driver.find_element(By.XPATH, "//ul/li[1]//a[@class='price']")
    first_product_price.click()
    time.sleep(2)

actions = [hover_first_product]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    # Click on the first advertisement link
    click_ad_link(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_ad.png')
    # Hover over the first product
    hover_first_product(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover_product.png')
    # Click on the first product image
    click_first_product_image(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_product_image.png')
    # Click on the first product comment link
    click_first_product_comment(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_product_comment.png')
    # Click on the first product price link
    click_first_product_price(driver)
    driver.save_screenshot(f'{dir}/_images/after_click_product_price.png')
