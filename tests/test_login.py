from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(setup):
    driver =setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    login.login("Admin", "admin123")
    assert dashboard.isdashboard_displayed()


def test_invalid_login(setup):
    driver =setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    login.login("joshi", "admin123")
    assert dashboard.isdashboard_displayed()