from django.db import models

# Create your models here.
class Base(models.Model):
    nombre = models.CharField(max_length=25)