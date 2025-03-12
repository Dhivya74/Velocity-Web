import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def click_element(driver, by_type, locator, timeout=10):
    """Waits for an element to be clickable and clicks it."""
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by_type, locator))).click()
        logger.info(f"Clicked element: {locator}")
    except Exception as e:
        logger.error(f"Error clicking element {locator}: {e}")


def wait_for_element(driver, by_type, locator, timeout=20):
    """Waits for an element to be present and returns it."""
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by_type, locator)))
        logger.info(f"Element found: {locator}")
        return element
    except Exception as e:
        logger.error(f"Error waiting for element {locator}: {e}")
        return None


def switch_to_new_tab(driver):
    """Switches to the newly opened browser tab."""
    try:
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        logger.info("Switched to new tab.")
    except Exception as e:
        logger.error(f"Error switching to new tab: {e}")


def close_and_switch_back(driver):
    """Closes the current window and switches back to the first opened window."""
    try:
        original_window = driver.window_handles[0]
        driver.close()
        driver.switch_to.window(original_window)
        logger.info("Closed current tab and switched back to main window.")
    except Exception as e:
        logger.error(f"Error closing tab and switching back: {e}")


def is_element_displayed(driver, by_type, locator, timeout=20):
    """Checks if an element is displayed on the page."""
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by_type, locator)))
        logger.info(f"Element displayed: {locator}")
        return element.is_displayed()
    except Exception as e:
        logger.error(f"Error checking element visibility {locator}: {e}")
        return False


def log_and_validate(driver, expected_text, log_file="test_log.txt"):
    """
    Logs the title and validates page content.
    """
    try:
        page_title = expected_text
        with open(log_file, "a") as file:
            file.write(f"Help Page Title: {page_title}\n")

        assert expected_text in driver.page_source, f"Incorrect Help page opened, expected: {expected_text}"
        logger.info(f"Validation successful for: {expected_text}")
    except Exception as e:
        logger.error(f"Error validating help page content: {e}")


def scroll_to_element(driver, by_type, locator):
    """Scrolls the page until the specified element is visible."""
    try:
        element = driver.find_element(by_type, locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        logger.info(f"Scrolled to element: {locator}")
    except Exception as e:
        logger.error(f"Error scrolling to element {locator}: {e}")
