from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import News, AddPost, DeletePost

urlpatterns = [
                  path('', News.as_view(), name='news'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
