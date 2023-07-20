from django import forms
from . import models


CHOICES_BOOK = [
    ('manga', 'Manga'),
    ('comic', 'Comic'),
    ('book','Book')
]

class BookForm(forms.ModelForm):
    booktype = forms.ChoiceField(choices=CHOICES_BOOK, label="Book type")
    class Meta:
        model = models.Book
        fields = '__all__'


