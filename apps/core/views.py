from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms
from django.contrib.auth.decorators import login_required
# Create your views here.

def start(request):
    return  render(request,'home.html')

def Aboutus(request):
    return render(request,'About.html')


# books folder views
@login_required
def Index(request):
    Books = models.Book.objects.all()
    context = {"Books": Books}

    if request.method == 'POST':
       typefilter = request.POST.get('selection', None)
       print(typefilter)
       Books = models.Book.objects.filter(booktype = typefilter)
       context["Books"] = Books
       return render(request, 'books/index.html',context)

    return render(request, 'books/index.html',context)
@login_required
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

@login_required
def editBookForm(request, id):
    book = models.Book.objects.get(id = id)
    form = forms.BookForm(request.POST or None, request.FILES or None, instance = book)
    print(form)
    context = { 'forms': form}
    return render(request,'books/editbook.html', context)
@login_required
def deleteBook(request, id):
    book = models.Book.objects.get(id = id)
    book.delete()
    return redirect('Books')