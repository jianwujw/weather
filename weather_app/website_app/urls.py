from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index),
    # path('log/',views.log),
    # path('authenticate_login/', views.authenticate_login),
    # path('register/',views.register),
    # path('authenticate_register/', views.authenticate_register),
    # path('logout/', LogoutView.as_view()),
]