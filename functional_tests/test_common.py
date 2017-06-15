from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from park.models import Animal
import os
import time


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.create_animal_data_for_test()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_home_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        time.sleep(1)
        self.assertIn('Animal', self.browser.title)
        
        button_list = self.browser.find_element_by_class_name('list_button').text
        self.assertIn('All', button_list)
        self.assertIn('Mammal', button_list)
        self.assertIn('Reptile', button_list)
        self.assertIn('Bird', button_list)
        self.assertIn('Amphibian', button_list)
        self.assertIn('Fish', button_list)
        
        self.browser.find_element_by_xpath("//button[@id='All']").click()
        time.sleep(1)
        
        self.browser.find_element_by_xpath("//button[@id='Cat']").click()
        time.sleep(1)
        
        info_text = self.browser.find_element_by_xpath("//div[@id='data']").text
        self.assertIn('Cat', info_text)
        habitat_text = self.browser.find_element_by_xpath("//div[@id='habitat']").text
        self.assertIn('ทุกๆที่บนโลกนี้', habitat_text)
        time.sleep(1)
        
    def create_animal_data_for_test(self):
        animal = Animal(thai_name = "แมว",
                        name = "Cat",
                        class_name = "Mammal",
                        order = "Carnivora",
                        family = "Felidae",
                        info = "แมวเหมียวน่ารัก ใครๆก็รักแมวเหมียว",
                        habitat = "ทุกๆที่บนโลกนี้ เจ้าแมวได้ครองโลกแล้ว",
                        status = "Published")
        animal.save()