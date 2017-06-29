from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from .models import Animal
from park.views import *
import re

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertIn('Animals', response.content.decode())
        expected_html = render_to_string(
        'park/home.html',
        {'all_animal':Animal.objects.filter(status="Published").count(),
            'mammal_num':Animal.objects.filter(status="Published",class_name="Mammal").count(),
            'reptile_num':Animal.objects.filter(status="Published",class_name="Reptile").count(),
            'bird_num':Animal.objects.filter(status="Published",class_name="Bird").count(),
            'fish_num':Animal.objects.filter(status="Published",class_name="Fish").count(),
            'amphibian_num':Animal.objects.filter(status="Published",class_name="Amphibian").count()}
        )
        self.assertEqual(response.content.decode(), expected_html)

        
class ListPageTest(TestCase):

    def test_root_url_resolves_to_list_page_view(self):
        found = resolve('/All/')
        self.assertEqual(found.func, animal_list)
      
    def test_list_page_return_correct_html(self):
        request = HttpRequest()
        response = animal_list(request,"All")
        self.assertIn('Animal List', response.content.decode())
        all_class = ["All","Mammal","Reptile","Bird","Fish","Amphibian"]
        list = Animal.objects.filter(status="Published").order_by('thai_name')
        
        class_name = "All"
        expected_html = render_to_string(
        'park/animal_list.html',{'lists':list,'all_class':all_class,'class_now':class_name})
        self.assertEqual(response.content.decode(), expected_html)
        
        response = animal_list(request,"Mammal")
        class_name = "Mammal"
        expected_html = render_to_string(
        'park/animal_list.html',{'lists':animal_list,'all_class':all_class,'class_now':class_name})
        self.assertEqual(response.content.decode(), expected_html)
        
    def test_no_page(self):
        request = HttpRequest()
        response = animal_list(request,"Myth")
        expected_html = render_to_string('park/no_page.html')
        self.assertEqual(response.content.decode(), expected_html)
        

class DataPageTest(TestCase):

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
        
        animal = Animal(thai_name = "สุนัข",
                        name = "Dog",
                        class_name = "Mammal",
                        order = "Carnivora",
                        family = "Canidae",
                        info = "สัตว์เลี้ยงผู้ซื่อสัตย์ และพร้อมจะเป็นเพื่อนกับมนุษย์ได้ทุกเวลา",
                        habitat = "บ้านคน, วัด, ข้างถนน, หน้ามินิมาร์ท",
                        status = "Pending")
        animal.save()

    def test_root_url_resolves_to_data_page_view(self):
        found = resolve('/animal/Cat')
        self.assertEqual(found.func, animal_data)
        
    def test_data_page_return_correct_html(self):
        self.create_animal_data_for_test()
        request = HttpRequest()
        response = animal_data(request,"Cat")
        
        animal = Animal.objects.get(name="Cat".replace('_', ' '))
        expected_html = render_to_string('park/animal_data.html',{'animal':animal})
        self.assertEqual(re.sub(r'<[^>]*csrfmiddlewaretoken[^>]*>', '', response.content.decode()),
                         re.sub(r'<[^>]*csrfmiddlewaretoken[^>]*>', '', expected_html))
        
    def test_no_page(self):
        self.create_animal_data_for_test()
        request = HttpRequest()
        response = animal_data(request,"Dog")
        
        animal = Animal.objects.get(name="Dog".replace('_', ' '))
        if(animal.status == "Pending"):
            expected_html = render_to_string('park/no_page.html')
            self.assertEqual(response.content.decode(), expected_html)
        else:
            raise
            

class SearchPageTest(TestCase):

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
        
    def test_root_url_resolves_to_search_page_view(self):
        found = resolve('/search/')
        self.assertEqual(found.func, search)
      
    def test_search_page_return_correct_html(self):
        self.create_animal_data_for_test()
        request = HttpRequest()
        response = search(request)
        self.assertIn('Search', response.content.decode())
        
        expected_html = render_to_string('park/search.html')
        self.assertEqual(response.content.decode(), expected_html)
        
    def test_search_data(self):
        self.create_animal_data_for_test()
        response = self.client.get('/search/', data={'word': 'Cat', 'search': 'all'})
        self.assertIn('แมว ( Cat )', response.content.decode())
        
        response = self.client.get('/search/', data={'word': 'Felidae', 'search': 'family'})
        self.assertIn('แมว ( Cat )', response.content.decode())
        
        
class AddPendingTest(TestCase):

    def test_root_url_resolves_to_add_animal_page_view(self):
        found = resolve('/add_animal/')
        self.assertEqual(found.func, add_pending)
        
    def test_add_animal_page_return_correct_html(self):
        response = self.client.get('/add_animal/', {'thai_name' : 'แมว',
                        'name' : 'Cat',
                        'class_name' : 'Mammal',
                        'order' : 'Carnivora',
                        'family' : 'Felidae',
                        'info' : 'แมวเหมียวน่ารัก ใครๆก็รักแมวเหมียว',
                        'habitat' : 'ทุกๆที่บนโลกนี้ เจ้าแมวได้ครองโลกแล้ว',
                        'submit' : "Submit"})
        self.assertIn('Add Animal Data', response.content.decode())
        
        expected_html = render_to_string('park/add_data.html')
        self.assertEqual(re.sub(r'<[^>]*csrfmiddlewaretoken[^>]*>', '', response.content.decode()),
                         re.sub(r'<[^>]*csrfmiddlewaretoken[^>]*>', '', expected_html))
                         
class AboutPageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/about/')
        self.assertEqual(found.func, about)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = about(request)
        self.assertIn('About', response.content.decode())
        expected_html = render_to_string('park/about.html')
        self.assertEqual(response.content.decode(), expected_html)