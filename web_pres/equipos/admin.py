from django.contrib import admin

# Register your models here.
from .models import Equipo

class EquipoAdmin(admin.ModelAdmin):
    readonly_fields =('ingresado','prestamo')
admin.site.register(Equipo,EquipoAdmin)
