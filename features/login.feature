Feature: OrangeHRM Login
  Scenario: valid user login
    Given Launch the browser and enter the url
    When Enter valid username and valid password
    And User clicks the login button
    Then user should see dashboardpage
