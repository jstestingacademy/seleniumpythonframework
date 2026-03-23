Feature: OrangeHRM Login

Scenario: valid user login
  Given launch the browser and enter the url
  When Enter valid username and valid password
  And User clicks the login button
  Then user should see dashboard page