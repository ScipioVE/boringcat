from django import forms
from . import models


CHOICES_BOOK = [
    ('manga', 'Manga'),
    ('comic', 'Comic'),
    ('book','Book')
]
CHOICES_FRONTPAGE = [
    (True, True),
    (False, False)
]

class BookForm(forms.ModelForm):
    booktype = forms.ChoiceField(choices=CHOICES_BOOK, label="Book type")
    front_page = forms.ChoiceField(choices=CHOICES_FRONTPAGE, label="Is a front page book")
    class Meta:
        model = models.Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            print(field)
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder':field.capitalize()})


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 40, 'cols': 100, 'placeholder': 'Content here'})
        }


##########################################
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Write your comment here...'})
        }

###########################################