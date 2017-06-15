from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from .models import Animal

from park.views import index

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
