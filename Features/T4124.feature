@regression @functional @T4124
Feature: Expansion Relays Help Functionality

  Scenario: Validate help icon and modal for Expansion Relays
    Given I log in to the application
    When the operator navigates to "DIGI*TRAC Configuration → Expansion Relays"
    Then the Help icon should be available on the top right
    When clicking that help icon
    Then "https://localhost/VWSC/Content/Help/ExpansionRelays.html" link should open in a new browser tab
    And Expansion Relays related information should be available
    When clicking Edit Expansion Relays
    Then the Edit Expansion Relays modal should open
    And the Edit Help icon should be available on the top right
    When clicking the Help icon within the modal
    Then "https://localhost/VWSC/Content/Help/ExpansionRelays.html" should open with Expansion Relays related information
