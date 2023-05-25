from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView

from auth_api import views

urlpatterns = [
    path('', views.check, name='check'),
    path('register', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('refresh-token', views.refresh_token, name='refresh_token'),
    path('refresh-token/', views.refresh_token, name='refresh_token'),
    path('logout', views.logout, name='logout'),
    path('logout/', views.logout, name='logout'),
    path('verify-token', views.verify_token, name='verify_token'),
    path('verify-token/', views.verify_token, name='verify_token'),
]