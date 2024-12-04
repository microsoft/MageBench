
def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

actions = []

def interact(driver, dir):
    # Save the initial state of the webpage
    save_initial_screenshot(driver, dir)
