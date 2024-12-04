
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def fill_nickname(driver):
    nickname_input = driver.find_element(By.XPATH, "//td[text()='昵称：']/following-sibling::td/input")
    nickname_input.send_keys("测试昵称")
    time.sleep(1)

def select_residence(driver):
    country_select = driver.find_element(By.XPATH, "//td[text()='居住地：']/following-sibling::td/select[1]")
    country_select.click()
    country_option = driver.find_element(By.XPATH, "//option[@value='美国']")
    country_option.click()
    time.sleep(1)

def select_gender(driver):
    gender_radio = driver.find_element(By.XPATH, "//input[@name='sex' and @value='female']")
    gender_radio.click()
    time.sleep(1)

def select_identity(driver):
    identity_radio = driver.find_element(By.XPATH, "//input[@name='identity' and @value='教师']")
    identity_radio.click()
    time.sleep(1)

def fill_hobbies(driver):
    hobbies_textarea = driver.find_element(By.XPATH, "//td[text()='兴趣爱好：']/following-sibling::td/textarea")
    hobbies_textarea.send_keys("阅读 旅行 音乐")
    time.sleep(1)

actions = []

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Perform actions and save screenshots after each action
    for action in actions:
        action(driver)
        driver.save_screenshot(f'{dir}/_images/{action.__name__}.png')
