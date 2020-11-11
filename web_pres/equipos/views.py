from django.shortcuts import render, get_object_or_404
from .models import Equipo

# Create your views here.

def verEquipos(request):
    equipos = Equipo.objects.all().filter(estado=True)
    return render(request,"equipos.html",{"equipos":equipos})

def detalleEquipos(request, prod_id):
    equipo = get_object_or_404(Equipo, id = prod_id)
    return render(request, "ver_equipos.html",{"equipo":equipo})

