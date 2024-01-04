from rest_framework import serializers
from .models import Paciente, Doctor, Cita


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('id', 'nombre', 'edad', 'email', 'motivo', 'fecha_nacimiento')


class DoctorSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer()

    class Meta:
        model = Doctor
        fields = ('id', 'nombre', 'apellido', 'sexo', 'email', 'especialidad', 'paciente')


class CitaSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    paciente = PacienteSerializer()

    class Meta:
        model = Cita
        fields = ('id', 'doctor', 'paciente', 'fecha', 'hora')
