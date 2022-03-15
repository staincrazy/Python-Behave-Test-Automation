# Created by reanoldpiatrenka at 15/03/2022
Feature: User is able to login to OrangeHRM application using correct credentials
  # Enter feature description here

  Scenario Outline: Navigate to the application
    Given I navigate to "<application_url>"
    Then I see proper "<page_title>"
    Examples:
    |application_url|page_title|
    |https://opensource-demo.orangehrmlive.com/index.php|OrangeHRM|
    |https://opensource-demo.orangehrmlive.com/index.php|Hello, World|