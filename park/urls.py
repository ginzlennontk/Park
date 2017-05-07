from django.conf.urls import url
from . import views

app_name = 'park'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^add_animal/$', views.add_pending, name='add_animal'),
    url(r'^(?P<class_name>[A-Za-z]+)/$', views.animal_list, name='animal_list'),
    url(r'^animal/(?P<animal_name>[A-Za-z_]+)$', views.animal_data, name='animal_data'),
    url(r'^animal/(?P<animal_name>[A-Za-z_]+)/add_pic/$', views.add_picture, name='add_picture'),
]

