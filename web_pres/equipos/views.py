from django.shortcuts import render
from .models import Equipo

# Create your views here.

def verEquipos(request):
    equipos = Equipo.objects.all().filter(estado=True)
    return render(request,"equipos.html",{"equipos":equipos})
