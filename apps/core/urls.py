from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.start,name='Home'),
    path('About', views.Aboutus,name='About'),
    path('Books', views.Index,name='Books'),
    path('Books/new_book', views.newBookForm,name='NewBook'),
    path('Books/edit_book', views.editBookForm,name='EditBook'),
    path('delete_book/<int:id>', views.deleteBook, name='DeleteBook'),
    path('Books/edit_book/<int:id>', views.editBookForm, name='EditBook'),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)