from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registration', views.registration),
    path('login', views.login_user),
    path('logout', views.logout_user),
]
