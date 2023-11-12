"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('dashboard/', views.profile, name='dashboard'),
    # path('add/', views.add, name='add'),
    # path('registration/', views.registration, name='registration'),
]