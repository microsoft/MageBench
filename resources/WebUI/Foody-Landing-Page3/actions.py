
def save_initial_screenshot(driver, dir):
    driver.save_screenshot(f'{dir}/_images/origin.png')

actions = []

def interact(driver, dir):
    # Save the original UI
    save_initial_screenshot(driver, dir)
