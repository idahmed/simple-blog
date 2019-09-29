from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='post'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
]


