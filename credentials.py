import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def click_element(driver, by_type, locator, timeout=10):
    """Waits for an element to be clickable and clicks it."""
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by_type, locator))).click()

def wait_for_element(driver, by_type, locator, timeout=10):
    """Waits for an element to be present and returns it."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by_type, locator)))

def switch_to_new_tab(driver):
    """Switches to the newly opened browser tab."""
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[1])

def close_and_switch_back(driver):
    """Closes the current tab and switches back to the main window."""
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def is_element_displayed(driver, by_type, locator, timeout=10):
    """Checks if an element is displayed on the page."""
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by_type, locator)))
    return element.is_displayed()


def log_and_validate(driver, expected_text, log_file="test_log.txt"):
    """
    Switches to the new tab, logs the title, and validates page content.

    :param driver: Selenium WebDriver instance
    :param expected_text: Expected text to verify on the page
    :param log_file: File to store the logs
    """
    page_title = expected_text
    with open(log_file, "a") as file:
        file.write(f"Help Page Title: {page_title}\n")

    assert expected_text in driver.page_source, f"Incorrect Help page opened, expected: {expected_text}"
    close_and_switch_back(driver)
