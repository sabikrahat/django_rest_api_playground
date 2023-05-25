from django.urls import path

from blog_api import views

urlpatterns = [
    path('', views.check, name='check'),
    path('create', views.create, name='create'),
    path('create/', views.create, name='create'),
    path('posts', views.posts, name='create'),
    path('posts/', views.posts, name='posts'),
]