from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.contrib.auth.decorators import login_required
# Create your views here.

def start(request):
    frontbooks = models.Book.objects.filter(front_page = True)
    context = { 'frontbooks' : frontbooks}
    return  render(request,'home.html', context)

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
    context = { 'forms': form}
    if form.is_valid():
     form.save()
    return render(request,'books/editbook.html', context)
@login_required
def deleteBook(request, id):
    book = models.Book.objects.get(id = id)
    book.delete()
    return redirect('Books')

#########################################################
def post_detail(request, id):
    post = get_object_or_404(models.Post, pk=id)
    context = {'Post': post}

    if request.method == 'POST':
        commentform = forms.CommentForm(request.POST)
        if commentform.is_valid():
           obj = commentform.save(commit=False)
           obj.parent = post
           obj.name = request.user.username
           obj.save()

           return redirect('Post',id)
    else:
        commentform = forms.CommentForm()
    

    

    context.update({'commentsForm':commentform})
   
    return render(request,'posts/post_detail.html', context)

############################################################

def postForm(request):
    form = forms.PostForm(request.POST or None, request.FILES or None)
    test = form.is_valid() 
    if test :
        form.save()
        return redirect('Books')
    else:
        print("ERROR!!")
    context = { 'forms': form}
    return render(request,'posts/post_form.html', context)

def editPostForm(request, id):
    Post = models.Post.objects.get(id = id)
    form = forms.PostForm(request.POST or None, request.FILES or None, instance = Post)
    if form.is_valid():
     form.save()
     return redirect('Books')
    context = { 'forms': form}
    return render(request,'posts/edit_post.html', context)



def catalog(request):
     Books = models.Book.objects.all()
     context = {"Books": Books}

     if request.method == 'POST':
         typefilter = request.POST.get('selection', None)
         Books = models.Book.objects.filter(booktype = typefilter)
         context["Books"] = Books
         return render(request, 'books/catalog.html',context)
     
     return render(request, 'books/catalog.html',context)