
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def hover_card_free(driver):
    card = driver.find_element(By.XPATH, "//div[@class='card'][1]")
    actions = ActionChains(driver)
    actions.move_to_element(card).perform()
    time.sleep(2)

def hover_card_standard(driver):
    card = driver.find_element(By.XPATH, "//div[@class='card'][2]")
    actions = ActionChains(driver)
    actions.move_to_element(card).perform()
    time.sleep(2)

actions = [hover_card_free, hover_card_standard]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Scroll the page
    scroll_page(driver)
    driver.save_screenshot(f'{dir}/_images/origin_scrolled.png')
    
    # Hover over the Free card
    hover_card_free(driver)
    driver.save_screenshot(f'{dir}/_images/hover_free.png')
    
    # Hover over the Standard card
    hover_card_standard(driver)
    driver.save_screenshot(f'{dir}/_images/hover_standard.png')
