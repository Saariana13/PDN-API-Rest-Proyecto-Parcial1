from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.CharField(max_length=50, null=True)
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'

class Doctor(models.Model):

    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50, default='Médico General')
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f'{self.id} - {self.apellido} {self.nombre}'

class Cita(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
