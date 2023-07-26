from django.db import models

# Create your models here.

class  num(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")