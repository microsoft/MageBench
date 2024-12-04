
from selenium.webdriver.common.by import By
import time

def change_loan_amount(driver):
    loan_amount_input = driver.find_element(By.ID, 'loan-amount')
    loan_amount_input.clear()
    loan_amount_input.send_keys('20000')
    time.sleep(1)  # wait for the calculation to complete

def change_interest_rate(driver):
    interest_rate_input = driver.find_element(By.ID, 'interest-rate')
    interest_rate_input.clear()
    interest_rate_input.send_keys('5')
    time.sleep(1)  # wait for the calculation to complete

def change_months_to_pay(driver):
    months_to_pay_input = driver.find_element(By.ID, 'months-to-pay')
    months_to_pay_input.clear()
    months_to_pay_input.send_keys('24')
    time.sleep(1)  # wait for the calculation to complete

actions = [change_loan_amount, change_interest_rate, change_months_to_pay]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Change loan amount
    change_loan_amount(driver)
    driver.save_screenshot(f'{dir}/_images/after_change_loan_amount.png')
    
    # Change interest rate
    change_interest_rate(driver)
    driver.save_screenshot(f'{dir}/_images/after_change_interest_rate.png')
    
    # Change months to pay
    change_months_to_pay(driver)
    driver.save_screenshot(f'{dir}/_images/after_change_months_to_pay.png')
