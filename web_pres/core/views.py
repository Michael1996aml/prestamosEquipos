from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def pag2(request):
    return render(request, "pag2.html")

def pag3(request):
    return render(request, "pag3.html")