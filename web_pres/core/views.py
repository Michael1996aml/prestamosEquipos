from django.shortcuts import render
from equipos.models import Equipo
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
equipos = Equipo.objects.all()


def home(request):
    return render(request, "home.html",{'equipos':equipos})


#def contacto(request):
 #   if request.method=="POST":
  #      message = request.POST["mansaje"] +" "+ request.POST["email"]
   #     email_from = settings.EMAIL_HOST_USER
    #    recipient_list = ["zendoo33@gmail.com"]
     #   send_mail(message, email_from, recipient_list)

  # return render(request, "home.html")