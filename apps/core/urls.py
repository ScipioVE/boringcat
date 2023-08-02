from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.start,name='Home'),
    path('About', views.Aboutus,name='About'),
    path('Admin/Books', views.Index,name='Books'),
    path('Admin/Books/new_book', views.newBookForm,name='NewBook'),
    path('Admin/Books/edit_book', views.editBookForm,name='EditBook'),
    path('Admin/delete_book/<int:id>', views.deleteBook, name='DeleteBook'),
    path('Admin/Books/edit_book/<int:id>', views.editBookForm, name='EditBook'),
    path('Book/Post/<int:id>', views.post_detail, name='Post'),
    path('Admin/Book/Post/New', views.postForm, name = 'PostForm'),
    path('Admin/Book/post_edit/<int:id>', views.editPostForm, name= 'EditPost'),
    path('Catalog', views.catalog, name= 'Catalog'),
    
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)