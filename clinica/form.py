from django import forms
from .models import Consulta

class Consultaform(forms.ModelForm):
    class Meta:
        model= Consulta
        fields= ['paciente', 'data', 'medico', 'status']