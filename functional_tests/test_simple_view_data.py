from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from park.models import Animal
import time


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.create_animal_data_for_test()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_home_and_retrieve_it_later(self):
        #คุณสมิธอยากจะรู้เรื่องข้อมูลถิ่นที่อยู่ของเจ้าแมวเหมียว เขาจึงเปิดเว็บแอพ Animal ขึ้นมา
        self.browser.get(self.live_server_url)
        time.sleep(1)
        
        #คุณสมิธทำการตรวจเช็คดูว่าเขาเข้าถูกแอพหรือไม่
        self.assertIn('Animal', self.browser.title)
        
        #คุณสมิธนั่งเพ่งมองไปที่ปุ่มประเภทของสัตว์ว่ามีอะไรบ้าง
        button_list = self.browser.find_element_by_class_name('list_button').text
        self.assertIn('All', button_list)
        self.assertIn('Mammal', button_list)
        self.assertIn('Reptile', button_list)
        self.assertIn('Bird', button_list)
        self.assertIn('Amphibian', button_list)
        self.assertIn('Fish', button_list)
        
        #แต่คุณสมิธไม่รู้ว่าเจ้าแมวเหมียวเป็นสัตว์ประเภทไหน เขาจึงกดเลือกไปที่ปุ่มสัตว์ทั้งหมด
        self.browser.find_element_by_name("All").click()
        time.sleep(1)
        
        #อ่า นั่นไงปุ่มของเจ้าแมวเหมียว เขาไม่รีรอที่จะเลื่อนเมาส์ไปกดที่ปุ่มนั่น
        self.browser.find_element_by_name("Cat").click()
        time.sleep(1)
        
        #คุณสมิธทำการตรวจเช็คให้แน่ใจว่านี่คือข้อมูลของเจ้าแมวเหมียว
        info_text = self.browser.find_element_by_name("data").text
        self.assertIn('Cat', info_text)
        
        #ในที่สุด คุณสมิธก็พบว่าถิ่นที่อยู่ของเจ้าแมวเหมียวนั่นก็คือ ทุกๆที่บนโลกน้นั่นเอง!!
        habitat_text = self.browser.find_element_by_name("habitat").text
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