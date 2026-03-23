from pytest_bdd import given, when, then, parsers

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utlities import config   # your custom name is fine

@given("launch the browser and enter the url")
def launch_browser():
    print("Browser launched")

@when("Enter valid username and valid password")
def enter_valid_username_password(setup):
    login = LoginPage(setup)
    login.enter_username(config.username)
    login.enter_password(config.password)

@when("User clicks the login button")
def click_login(setup):
    login = LoginPage(setup)
    login.click_login()

@then("user should see dashboard page")
def verify_dashboard(setup):
    dashboard = DashboardPage(setup)
    assert dashboard.isdashboard_displayed()