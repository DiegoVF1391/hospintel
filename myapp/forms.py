from django import forms
from .models import Image, Paciente

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido_paterno', 'apellido_materno','domicilio', 'sexo', 'edad', 'fecha_nacimiento', 'correo', 'telefono')