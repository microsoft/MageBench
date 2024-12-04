
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_add_note_button(driver):
    add_button = driver.find_element(By.ID, 'btn')
    add_button.click()
    time.sleep(1)  # wait for the note to be added

def type_in_note_field(driver):
    note_field = driver.find_element(By.CLASS_NAME, 'note')
    note_field.send_keys("This is a test note.")
    time.sleep(1)  # wait for the input to be registered

def double_click_to_delete_note_field(driver):
    note_field = driver.find_element(By.CLASS_NAME, 'note')
    actions = ActionChains(driver)
    actions.double_click(note_field).perform()
    time.sleep(1)  # wait for the confirmation prompt


actions = [click_add_note_button, type_in_note_field, double_click_to_delete_note_field]

def interact(driver, dir):
    # save the original UI
    driver.save_screenshot(f'{dir}/_images/origin.png') 
    # click add note button
    click_add_note_button(driver)
    # save after adding note
    driver.save_screenshot(f'{dir}/_images/after_add_note.png') 
    # type in the note field
    type_in_note_field(driver)
    # save after typing in note
    driver.save_screenshot(f'{dir}/_images/after_typing_note.png') 
    # double click to delete note
    double_click_to_delete_note_field(driver)
    # save after deleting note
    driver.save_screenshot(f'{dir}/_images/after_deleting_note.png') 
