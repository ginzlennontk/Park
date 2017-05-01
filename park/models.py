from django.db import models
from uuid import uuid4
import os

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
    class_name = models.CharField(max_length=200)
    order = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    info = models.TextField(null=True, blank=True)
    habitat = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to=path_and_rename,null=True, blank=True)

    def __str__(self):
        return self.name

class Pending(models.Model):
    thai_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=200)
    order = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    info = models.TextField(null=True, blank=True)
    habitat = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='pending_pic/',null=True, blank=True)

    def __str__(self):
        return self.name
