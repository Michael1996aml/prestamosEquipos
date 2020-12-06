from django import forms
from .models import Prestamos,Equipo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = '__all__'
        widgets = {
            "fechad":forms.SelectDateWidget()
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        