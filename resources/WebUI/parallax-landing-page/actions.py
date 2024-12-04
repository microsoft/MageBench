
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def click_learn_more(driver):
    learn_more_button = driver.find_element(By.CLASS_NAME, 'btn')
    learn_more_button.click()
    time.sleep(2)

def hover_learn_more(driver):
    learn_more_button = driver.find_element(By.CLASS_NAME, 'btn')
    actions = ActionChains(driver)
    actions.move_to_element(learn_more_button).perform()
    time.sleep(2)

actions = [scroll_page]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Click the "Learn More" button
    click_learn_more(driver)
    driver.save_screenshot(f'{dir}/_images/after_click.png')
    
    # Hover over the "Learn More" button
    hover_learn_more(driver)
    driver.save_screenshot(f'{dir}/_images/after_hover.png')
