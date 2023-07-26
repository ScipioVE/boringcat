from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('signup/', views.signupform , name='signup'),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)