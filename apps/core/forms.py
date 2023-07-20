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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            print(field)
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder':field.capitalize()})
        

   