from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from news.views import AddPost, UpdatePost, DeletePost

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include("blog.urls")),
                  path('messenger', include("messenger.urls")),
                  path('user_profile', include('user_profile.urls')),
                  path('news', include('news.urls')),
                  path('add_post', AddPost.as_view(), name='add_post'),
                  path('update_post/<int:pk>', UpdatePost.as_view(), name='update_post'),
                  path('delete/<int:pk>', DeletePost.as_view(), name='delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
