from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.verEquipos, name="equipos"),
    path('equipo/<int:prod_id>',views.detalleEquipos,name="equipo")
]