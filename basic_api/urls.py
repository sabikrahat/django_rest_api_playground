from django.urls import path

from basic_api import views

urlpatterns = [
    path('', views.check, name='check'),
    path('addition', views.addition, name='addition'),
    path('addition/', views.addition, name='addition'),
]