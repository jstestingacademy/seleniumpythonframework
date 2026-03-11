from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    UserName= (By.NAME, "username")
    Password= (By.NAME, "password")
    login_btn= (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.enter_Text(self.UserName, username)

        self.enter_Text(self.Password, password)
        self.click_Button(self.login_btn)



