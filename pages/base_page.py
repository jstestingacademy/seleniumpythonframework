from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def enter_Text(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)
        
    def click_Button(self ,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_title(self):
        return self.driver.title