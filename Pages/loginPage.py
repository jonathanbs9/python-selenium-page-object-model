from Locators.locators import Locators
from Locators.locators import Locators
class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.login_button_id = Locators.login_button_id

        self.invalid_username_message_xpath = '//*[@id="spanMessage"]'

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)
    
    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_username(self):
        msg = self.driver.find_element_by_xpath(self.invalid_username_message_xpath).text
        return msg
