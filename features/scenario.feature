Feature: Add remove test on OrangeHRM

  Scenario: Add remove flow
    Given the driver is initialized
    When we login successfully
    And we go to the Admin panel
    And we add a new ESS user
    Then we check that the new ESS user is appeared in the list
    And we remove the row with the new ESS user
