from django.contrib import admin
from . import models
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body','post','created_on','active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments'] 

    def approve_comments(self,request,queryset):
        queryset.update(active =True)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
        

admin.site.register(models.Book)
admin.site.register(models.Comment)
admin.site.register(models.Post, PostAdmin)

