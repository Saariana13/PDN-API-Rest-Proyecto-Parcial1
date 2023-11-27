from django.http import HttpResponse
from django.forms import modelform_factory
from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from medico.models import Doctor
from medico.forms import MedicoFormulario

MedicoFormulario = modelform_factory(Doctor, exclude=['activo',])

def agregar_medico(request):
    pagina = loader.get_template('agregar.html')
    if request.method == "GET":
        formulario = MedicoFormulario
    elif request.method == "POST":
        formulario = MedicoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario':formulario}
    return HttpResponse(pagina.render(datos,request))

def ver_medico(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    datos = {'medico': doctor}
    pagina = loader.get_template('ver.html')
    return HttpResponse(pagina.render(datos, request))

def modificar_medico(request, id):
    pagina = loader.get_template('modificar.html')
    doctor = get_object_or_404(Doctor, pk=id)
    if request.method == 'GET':
        formulario = MedicoFormulario(instance=doctor)
    elif request.method == 'POST':
        formulario = MedicoFormulario(request.POST, instance=doctor)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def eliminar_medico(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    if doctor:
        doctor.delete()
        return redirect('inicio')