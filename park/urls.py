from django.conf.urls import url
from . import views

app_name = 'park'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<class_name>[A-Za-z]+)/$', views.animal_list, name='animal_list'),
    url(r'^animal/(?P<animal_id>[0-9]+)$', views.animal_data, name='animal_data'),
]

