from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
     path('profile-create/', views.CreateProfile.as_view(), name='profile-create'),
     path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
]