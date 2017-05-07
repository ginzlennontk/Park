from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
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
    upload_to = 'animal_pic/' + str(instance.animal.name)
    # get filename
    if instance.animal.name:
        filename = '{}.{}'.format(instance.animal.name, "jpg")
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, "jpg")
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
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,null=True, blank=True)

    def __str__(self):
        return self.name
    
    def url_name(self):
        return self.name.replace(' ', '_')

class AnimalImage(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=path_and_rename)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,null=True, blank=True)

@receiver(pre_delete, sender=AnimalImage)
def pic_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)