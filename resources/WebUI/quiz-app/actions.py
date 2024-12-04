
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def select_answer_for_quiz_1(driver):
    answer_element = driver.find_element(By.ID, 'd')  # Selecting the correct answer for the first question
    answer_element.click()
    time.sleep(1)

def submit_answer_for_quiz_1(driver):
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()
    time.sleep(1)

def select_and_submit_for_quiz_2(driver):
    answer_element = driver.find_element(By.ID, 'b')  # Selecting the correct answer for the second question
    answer_element.click()
    time.sleep(1)
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()
    time.sleep(1)

def select_and_submit_for_quiz_3(driver):
    answer_element = driver.find_element(By.ID, 'a')  # Selecting the correct answer for the third question
    answer_element.click()
    time.sleep(1)
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()
    time.sleep(1)

def select_and_submit_for_quiz_4(driver):
    answer_element = driver.find_element(By.ID, 'b')  # Selecting the correct answer for the fourth question
    answer_element.click()
    time.sleep(1)
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()
    time.sleep(1)

actions = [
    select_answer_for_quiz_1,
    submit_answer_for_quiz_1,
    select_and_submit_for_quiz_2,
    select_and_submit_for_quiz_3,
    select_and_submit_for_quiz_4
]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 

    # Select answer for quiz 1
    select_answer_for_quiz_1(driver)
    driver.save_screenshot(f'{dir}/_images/after_select_quiz_1.png') 

    # Submit answer for quiz 1
    submit_answer_for_quiz_1(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit_quiz_1.png') 

    # Select and submit for quiz 2
    select_and_submit_for_quiz_2(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit_quiz_2.png') 

    # Select and submit for quiz 3
    select_and_submit_for_quiz_3(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit_quiz_3.png') 

    # Select and submit for quiz 4
    select_and_submit_for_quiz_4(driver)
    driver.save_screenshot(f'{dir}/_images/after_submit_quiz_4.png') 
