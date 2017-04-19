from django.db import models

class Animals(models.Model):
    thai_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=200)
    order = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
