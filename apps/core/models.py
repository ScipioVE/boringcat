from typing import Any, Dict, Tuple
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Titulo")

    booktype = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/", null=True, verbose_name="Image")
    description = models.TextField(
        max_length=1000, verbose_name="Description", null=True, blank=True
    )
    publish_date = models.DateField(null=True)
    front_page = models.BooleanField(default=False)

    def __str__(self) -> str:
        data = "Title: " + self.title + "|" + "Description: " + self.description
        return data

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)

        return super().delete()


class Post(models.Model):
    STATUS =(
        (0,'WAITING'),
        (1,"PUBLISH")
    )

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Book, on_delete= models.CASCADE,related_name='book_posts')
    updated_on =models.DateTimeField(auto_now=True)
    content =models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = AutoSlugField(populate_from='title', unique=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


########################################
class Comment(models.Model):
    parent = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self) -> str:
        return "Comment on {} by {}".format(self.parent.title, self.name)
##############################################