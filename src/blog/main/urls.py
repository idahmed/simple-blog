from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='post'),
]


