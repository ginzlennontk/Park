from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from park.models import Animal
import time


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_home_and_retrieve_it_later(self):
        #คุณสมิธอยากจะเพิ่มข้อมูลของเจ้าแมวเหมียว ให้กับเว็บแอพ Animal
        self.browser.get(self.live_server_url)
        time.sleep(1)
        
        #คุณสมิธทำการตรวจเช็คดูว่าเขาเข้าถูกแอพหรือไม่
        self.assertIn('Animal', self.browser.title)
        
        #จากนั้นเขาจึงกดไปที่ปุ่ม add animal เพื่อที่จะเพิ่มข้อมูลของเจ้าแมวเหมียว
        self.browser.find_element_by_name("add_animal").click()
        time.sleep(1)
        
        #เขาทำการเช็คหน้าเว็บแอพให้แน่ใจว่าเขาเข้ามาที่หน้า add animal แลัว
        self.assertIn('Add Animal', self.browser.title)
        
        #แต่คุณสมิธดันมือลั่นไปกดปุ่ม submit ก่อนที่จะกรอกข้อมูล
        self.browser.find_element_by_name("submit").click()
        time.sleep(1)
        
        #เว็บแอพจึงแสดงข้อความแจ้งเตือนขึ้นมา
        message = self.browser.find_element_by_name("message").text
        self.assertIn("กรุณากรอกชื่อของสัตว์ด้วยจ้า", message)
        
        #จากนั้นคุณสมิธจึงค่อย ๆกรอกข้อมูลทั้งหมดของเจ้าแมวเหมียวลงไป แล้วจึงกดปุ่ม submit
        inputbox = self.browser.find_element_by_name('thai_name')
        inputbox.send_keys("แมว")
        
        inputbox = self.browser.find_element_by_name('name')
        inputbox.send_keys("Cat")
        
        inputbox = self.browser.find_element_by_name('class_name')
        inputbox.send_keys("Mammal")
        
        inputbox = self.browser.find_element_by_name('order')
        inputbox.send_keys("Carnivora")
        
        inputbox = self.browser.find_element_by_name('family')
        inputbox.send_keys("Felidae")
        
        inputbox = self.browser.find_element_by_name('info')
        inputbox.send_keys("แมวเหมียวน่ารัก ใครๆก็รักแมวเหมียว")
        
        inputbox = self.browser.find_element_by_name('habitat')
        inputbox.send_keys("ทุกๆที่บนโลกนี้ เจ้าแมวได้ครองโลกแล้ว")
        self.browser.find_element_by_name("submit").click()
        time.sleep(1)
        
        #จากนั้นว็บแอพก็แสดงข้อความแจ้งขึ้นมาขอบคุณ เมื่อคุณสมิธเห็นข้อความแล้วเขาก็เลยปิดคอมแล้วไปเล่นกับแมวของเขาต่อไป
        message = self.browser.find_element_by_name("message").text
        self.assertIn("ขอบคุณที่ช่วยเพิ่มข้อมูลให้กับเรา :)", message)
        