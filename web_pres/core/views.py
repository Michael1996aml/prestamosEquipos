from django.shortcuts import render
from equipos.models import Equipo

# Create your views here.
equipos = Equipo.objects.all()


def home(request):
    return render(request, "home.html",{'equipos':equipos})

def pag2(request):
    return render(request, "pag2.html")

def pag3(request):
    return render(request, "pag3.html")