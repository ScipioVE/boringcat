from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Titulo")
    
    
    booktype = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/',null=True, verbose_name="Image")
    description = models.TextField(verbose_name="Description",null=True)
   


    def __str__(self) -> str:
        data = "Title: " + self.title + "|" + "Description: " + self.description
        return data
    
    def delete(self, using = None, keep_parents = False ):
        self.image.storage.delete(self.image.name)
       
        return super().delete()