from django import forms
from . import models


class BookForm(forms.ModelForm):
   
   
    class Meta:
        model = models.Book
        fields = '__all__'
        widgets = {
            'booktype': forms.Select
        }