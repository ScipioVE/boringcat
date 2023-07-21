from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms

# Create your views here.

def start(request):
    return  render(request,'home.html')

def Aboutus(request):
    return render(request,'About.html')


# books folder views

def Index(request):
    Books = models.Book.objects.all()
    context = {"Books": Books}

    return render(request, 'books/index.html',context)

def newBookForm(request):
    form = forms.BookForm(request.POST or None, request.FILES or None)
    test = form.is_valid() 
    if test :
        form.save()
        return redirect('Books')
    else:
        print("ERROR!!")
    context = { 'forms': form}
    return render(request,'books/newbook.html', context)


def editBookForm(request, id):
    book = models.Book.objects.get(id = id)
    form = forms.BookForm(request.POST or None, request.FILES or None, instance = book)
    print(form)
    context = { 'form': form}
    return render(request,'books/editbook.html', context)

def deleteBook(request, id):
    book = models.Book.objects.get(id = id)
    book.delete()
    return redirect('Books')