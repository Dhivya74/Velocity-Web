"""
Author: Dhivya
Date: 05-03-2025
Input: URL from dynamic_variables
Output: Opens the webpage and verifies title
Function: Uses Selenium WebDriver to navigate to a webpage and handle login.
"""
import time
from driver_manager import start_driver
from dynamic_variables import URL, operator_name, password
from behave import given, when, then
from selenium.webdriver.common.by import By
from credentials import click_element, wait_for_element, switch_to_new_tab, close_and_switch_back, is_element_displayed,log_and_validate
from Pages.POM_T4124 import operator_name_id, username_id, login_btn_id, EDITHELP_CLASS, HELP_XPATH, DROPDOWN_ID, EDIT_ID, DEVICE_CONTROL_ID, EXPANSION_RELAY_ID, CHECKBOX_ID

@given('I log in to the application')
def step_login(context):
    """Logs into the application."""
    context.driver = start_driver() if not hasattr(context, "driver") else context.driver
    context.driver.get(URL)
    context.driver.maximize_window()
    wait_for_element(context.driver, By.ID, operator_name_id).send_keys(operator_name)
    wait_for_element(context.driver, By.ID, username_id).send_keys(password)
    click_element(context.driver, By.ID, login_btn_id)
    assert "Velocity" in context.driver.title, "Login failed!"

@when('the operator navigates to "DIGI*TRAC Configuration → Expansion Relays"')
def step_navigate_to_expansion_relays(context):
    """Navigates to Expansion Relays under DIGI*TRAC Configuration."""
    click_element(context.driver, By.ID, DEVICE_CONTROL_ID)
    click_element(context.driver, By.ID, EXPANSION_RELAY_ID)

@then('the Help icon should be available on the top right')
def step_validate_help_icon(context):
    """Validates the presence of the Help icon."""
    assert is_element_displayed(context.driver, By.XPATH, HELP_XPATH), "Help icon is not visible"

@when('clicking that help icon')
def step_click_help_icon(context):
    """Clicks the Help icon and validates the new tab opens."""
    click_element(context.driver, By.XPATH, HELP_XPATH)

@then('"https://localhost/VWSC/Content/Help/ExpansionRelays.html" link should open in a new browser tab')
def step_validate_help_page(context):
    """Switches to the new tab and verifies the correct Help page opened."""
    switch_to_new_tab(context.driver)
    assert "ExpansionRelays.html" in context.driver.current_url, "Incorrect Help page opened"
    close_and_switch_back(context.driver)

@then('Expansion Relays related information should be available')
def step_validate_expansion_relays_info(context):
    """Validates the presence of Expansion Relays related content."""
    assert "Expansion Relays" in context.driver.page_source, "Expected Expansion Relays content not found"

@when('clicking Edit Expansion Relays')
def step_click_edit_expansion_relays(context):
    """Clicks the Edit Expansion Relays button."""
    context.driver.find_element(By.ID,CHECKBOX_ID).click()
    context.driver.find_element(By.ID,DROPDOWN_ID).click()

@then('the Edit Expansion Relays modal should open')
def step_validate_modal(context):
    """Validates that the Edit Expansion Relays modal is open."""
    modal = wait_for_element(context.driver, By.ID, EDIT_ID)
    assert modal.is_displayed(), "Edit Expansion Relays modal is not visible"
    click_element(context.driver, By.ID, EDIT_ID)

@then('the Edit Help icon should be available on the top right')
def step_validate_modal_help_icon(context):
    """Validates the presence of the Help icon inside the modal."""
    assert is_element_displayed(context.driver, By.CLASS_NAME, EDITHELP_CLASS), "Modal Help icon is not visible"

@when('clicking the Help icon within the modal')
def step_click_modal_help_icon(context):
    """Clicks the Help icon inside the modal."""
    click_element(context.driver, By.CLASS_NAME, EDITHELP_CLASS)

@then('"https://localhost/VWSC/Content/Help/ExpansionRelays.html" should open with Expansion Relays related information')
def step_validate_modal_help_page(context):
    """Switches to the new tab and verifies the correct Help page opened for the modal."""
    log_and_validate(context.driver, "Expansion Relays")
