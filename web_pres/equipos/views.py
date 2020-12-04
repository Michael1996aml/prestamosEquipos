from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipo,Prestamos
from .forms import PrestamoForm
from django.contrib import messages



# Create your views here.

def verEquipos(request):
    equipos = Equipo.objects.all().filter(estado=True)
    return render(request,"equipos.html",{"equipos":equipos})

def detalleEquipos(request, prod_id):
    equipo = get_object_or_404(Equipo, id = prod_id)
    return render(request, "ver_equipos.html",{"equipo":equipo})

def agregar_prestamo(request):

    data = {
        'form': PrestamoForm()
    }

    if request.method == 'POST':
        formulario = PrestamoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(request,'prestamo/agregar_pres.html',data)

def listar_prestamos(request):
    prestamos = Prestamos.objects.all()
    data = {
        'prestamos': prestamos
    }


    return render(request,"prestamo/listar_pres.html",data)

def modificar_prestamo(request,id):
    prestamo = get_object_or_404(Prestamos, id=id)

    data = {
        'form': PrestamoForm(instance=prestamo)
    }

    if request.method == 'POST':
        formulario = PrestamoForm(data=request.POST, instance=prestamo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            return redirect(to="listar_pres")
        data["form"] = formulario

    return render(request,"prestamo/modificar_pres.html",data)

def eliminar_prestamo(request,id):
    prestamo = get_object_or_404(Prestamos, id=id)
    prestamo.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to='listar_pres')

   
