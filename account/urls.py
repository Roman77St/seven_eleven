from django.urls import path, include
from django.contrib.auth import views as auth_views


from .views import register

# app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
