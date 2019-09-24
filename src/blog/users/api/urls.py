from django.urls import path, include

from . import views

app_name = 'users-api'
urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='api-register'),
]