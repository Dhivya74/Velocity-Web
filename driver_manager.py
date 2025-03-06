"""
Author: Dhivya
Date: 04-03-2025
Input: URL
Output: Opened Webpage
Function: Initializes Chrome WebDriver and handles SSL errors.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def start_driver():
    """Initializes and returns the WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def quit_driver(driver):
    """Quits the WebDriver."""
    driver.quit()
