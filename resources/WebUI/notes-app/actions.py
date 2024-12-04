
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_add_note_button(driver):
    add_button = driver.find_element(By.ID, 'add')
    add_button.click()
    time.sleep(1)  # Wait for the note to be added

def enter_text_in_note_textarea(driver):
    text_area = driver.find_element(By.TAG_NAME, 'textarea')
    text_area.send_keys("This is a test note.")
    time.sleep(1)  # Wait for the text to be entered

def click_edit_button(driver):
    edit_button = driver.find_element(By.CLASS_NAME, 'edit')
    edit_button.click()
    time.sleep(1)  # Wait for the toggle to take effect

def delete_note_button(driver):
    delete_button = driver.find_element(By.CLASS_NAME, 'delete')
    delete_button.click()
    time.sleep(1)  # Wait for the note to be deleted

actions = [click_add_note_button, enter_text_in_note_textarea, click_edit_button, delete_note_button]

def interact(driver, dir):
    # Save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png')
    
    # Click add note button
    click_add_note_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_add_note.png')
    
    # Enter text in the note textarea
    enter_text_in_note_textarea(driver)
    driver.save_screenshot(f'{dir}/_images/after_enter_text.png')
    
    # Click edit button to toggle view
    click_edit_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_edit_toggle.png')
    
    # Delete the note
    delete_note_button(driver)
    driver.save_screenshot(f'{dir}/_images/after_delete_note.png')
