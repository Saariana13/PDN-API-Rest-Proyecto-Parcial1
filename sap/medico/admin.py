from django.contrib import admin
from medico.models import Paciente, Cita, Doctor

admin.site.register(Paciente)
admin.site.register(Cita)
admin.site.register(Doctor)
