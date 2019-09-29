from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
]