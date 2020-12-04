from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.verEquipos, name="equipos"),
    path('equipo/<int:prod_id>',views.detalleEquipos,name="equipo"),
    path('agregar-prestamo/',views.agregar_prestamo,name="agregar_pres"),
    path('listar-prestamo/',views.listar_prestamos,name="listar_pres"),
    path('modificar-prestamo/<id>/',views.modificar_prestamo,name="modificar_pres"),
    path('eliminar-prestamo/<id>',views.eliminar_prestamo,name="eliminar_pres")
]