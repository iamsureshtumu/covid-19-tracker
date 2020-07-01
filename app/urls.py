from django.contrib import admin
from django.urls import path,re_path
from app import views

app_name="app"

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
]