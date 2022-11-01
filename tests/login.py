from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
import unittest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		chromedriver_autoinstaller.install()
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()

	def test_login_valid(self):
		driver = self.driver
		driver.get("https://opensource-demo.orangehrmlive.com/")

		login = LoginPage(driver)
		login.enter_username("Admin")
		login.enter_password("admin123")
		login.click_login()

		homepage = HomePage(driver)
		homepage.click_welcome()
		homepage.click_logout()

		time.sleep(2)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test Completed")

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/zennode/Documents/demo_workspace/automation/first_project/pom_project_demo/reports'))