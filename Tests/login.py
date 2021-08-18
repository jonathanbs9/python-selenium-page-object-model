from Locators.locators import Locators
from selenium import webdriver
import unittest

#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), "..",".." ))

from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

import HtmlTestRunner

class LoginTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.add_argument("start-maximized")
        cls.driver = webdriver.Chrome(options=cls.options, executable_path="./drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)        

    # Happy Path
    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home_page = HomePage(driver)
        home_page.click_welcome()
        home_page.click_logout()
    
    # Alternative Scenario 1
    def test_02_login_invalid_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("invalidAdmin")
        login.enter_password("admin123")
        login.click_login()

        message = login.check_invalid_username()
        self.assertEqual(message, "Invalid credentials")
    
    # Alternative Scenario 2
    def test_03_login_invalid_password(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("invalidPassword")
        login.click_login()

        message = login.check_invalid_username()
        self.assertEqual(message, "Invalid credentials")

    # Alternative Scenario 3
    def test_04_login_empty_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("")
        login.enter_password("admin123")
        login.click_login()

        message = login.check_invalid_username()
        self.assertEqual(message, "Username cannot be empty")
    
    # Alternative Scenario 4
    def test_04_login_empty_password(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("")
        login.click_login()

        message = login.check_invalid_username()
        self.assertEqual(message, "Password cannot be empty")

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ ==  '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Proyectos/Python/python-selenium-page-object-model/reports'))