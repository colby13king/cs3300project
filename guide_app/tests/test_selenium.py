import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QuestionSeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_create_question(self):
        # Assuming you have a page for creating questions that requires login
        self.selenium.get(f'{self.live_server_url}/login/')
        username_input = self.selenium.find_element(By.NAME, 'username')
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element(By.NAME, 'password')
        password_input.send_keys('mypassword')
        password_input.send_keys(Keys.RETURN)

        # Wait for redirect to question create page
        WebDriverWait(self.selenium, 10).until(
            EC.url_changes(f'{self.live_server_url}/login/')
        )

        # Navigate to the create question page
        self.selenium.get(f'{self.live_server_url}/question/add/')

        # Fill out the question form
        title_input = self.selenium.find_element(By.NAME, 'title')
        title_input.send_keys('What is Selenium?')
        body_input = self.selenium.find_element(By.NAME, 'body')
        body_input.send_keys('Can you explain what Selenium is used for in testing?')

        # Submit the form
        self.selenium.find_element(By.CSS_SELECTOR, 'form button').click()

        # Check if the question was created by looking for it on the questions page
        self.selenium.get(f'{self.live_server_url}/questions/')
        body_text = self.selenium.find_element(By.TAG_NAME, 'body').text
        self.assertIn('What is Selenium?', body_text)

# Repeat similar structure for other test cases