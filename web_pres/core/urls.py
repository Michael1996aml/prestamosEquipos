from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.pag2, name="pag2"),
    path('', views.pag3, name="pag3")
   
]