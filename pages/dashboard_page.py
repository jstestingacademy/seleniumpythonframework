

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    dashboard_header=(By.XPATH, "//h6[text()='Dashboard']")

    def isdashboard_displayed(self):
        return self.wait.until(lambda driver: driver.find_element(*self.dashboard_header)).is_displayed()

