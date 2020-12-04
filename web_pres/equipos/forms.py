from django import forms
from .models import Prestamos

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = '__all__'
        widgets = {
            "fechad":forms.SelectDateWidget()
        }

