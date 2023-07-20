from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.
class Booktype(models.Model):
    MANGA = 'manga'
    COMIC = 'comic'
    DEFAULT = 'book'
    CHOICES = [
        (MANGA, 'Manga'),
        (COMIC, 'Comic'),
        (DEFAULT,'book')
    ]
    
    name = models.CharField(choices=CHOICES, default=DEFAULT)

    def __str__(self) -> str:
        return "{}".format(self.get_name_display())


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Titulo")
    booktype = models.ForeignKey(Booktype,null= False,blank=False,on_delete= models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True, verbose_name="Image")
    description = models.TextField(verbose_name="Description",null=True)
   


    def __str__(self) -> str:
        data = "Title: " + self.title + "|" + "Description: " + self.description
        return data
    
    def delete(self, using = None, keep_parents = False ):
        self.image.storage.delete(self.image.name)
       
        return super().delete()