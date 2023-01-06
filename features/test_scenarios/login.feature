# Created on 15/03/2022
  # Updated on 5/01/2023

Feature: User is able to login to OrangeHRM application using correct credentials

  Scenario Outline: Navigate to the application
    Given I navigate to "<application_url>"
    Then I see proper "<page_title>"
    Examples:
    |application_url|page_title|
    |https://opensource-demo.orangehrmlive.com/index.php|OrangeHRM|
    |https://opensource-demo.orangehrmlive.com/index.php|Hello, World|

  Scenario Outline: Login to application
    Given I navigate to "<application_url>"
    When I enter username "<username>"
    And I enter password "<password>"
    And I click on login button
    Then I see dashboard
    Examples:
    |application_url|username|password|
    |https://opensource-demo.orangehrmlive.com/index.php|Admin|admin123|