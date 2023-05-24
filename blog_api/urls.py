from django.urls import path

from blog_api import views

urlpatterns = [
    path('', views.check, name='check'),
]