from django.forms import ModelForm, EmailInput
from medico.models import Doctor


class MedicoFormulario(ModelForm):
    class Meta:
        model = Doctor
        fields = ('nombre', 'apellido', 'sexo', 'email', 'especialidad')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }