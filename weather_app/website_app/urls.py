from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('log/',views.log),
    path('authenticate_login/', views.authenticate_login),
    path('register/',views.register),
    path('authenticate_register/', views.authenticate_register),
]