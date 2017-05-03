from django.db import models
from uuid import uuid4
import os

STATUS_CHOICES = (
    ('Pending','Pending'),
    ('Published','Published'),
)

CLASS_CHOICES = (
    ('Mammal','Mammal'),
    ('Reptile','Reptile'),
    ('Amphibian','Amphibian'),
    ('Fish','Fish'),
    ('Bird','Bird'),
)

def path_and_rename(instance, filename):
    upload_to = 'animal_pic'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Animal(models.Model):
    thai_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=10,choices=CLASS_CHOICES)
    order = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    info = models.TextField(null=True, blank=True)
    habitat = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to=path_and_rename,null=True, blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,null=True, blank=True)

    def __str__(self):
        return self.name

class AnimalImage(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField()