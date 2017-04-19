from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        self.browser.get('http://localhost:8000/park')
        self.assertIn('Park', self.browser.title)
        self.fail('Complete : No Error!')

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')
