*** Settings ***
Resource    login_resources.robot

*** Test Cases ***
Successful Login Using Gherkin
    Given I am on the login page 
    When I submit credentials  tomsmith  SuperSecretPassword! 
    Then I should see the secure area 
    And I close the browser