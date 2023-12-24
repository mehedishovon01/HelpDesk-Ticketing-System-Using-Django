"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.urls import path
from . import views


urlpatterns = [
    path('create', views.ticket_create, name='create-ticket'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/delete/<int:ticket_id>/', views.ticket_delete, name='ticket_delete'),
]
