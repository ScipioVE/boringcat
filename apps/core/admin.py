from django.contrib import admin
from . import models
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
        

admin.site.register(models.Book)
admin.site.register(models.Comment)
admin.site.register(models.Post, PostAdmin)

