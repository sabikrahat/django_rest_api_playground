from django.urls import path

from auth_api import views

urlpatterns = [
    path('', views.check, name='check'),
    path('register', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('refresh', views.refresh, name='refresh'),
    path('refresh/', views.refresh, name='refresh'),
    path('logout', views.logout, name='logout'),
    path('logout/', views.logout, name='logout'),
]