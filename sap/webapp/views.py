from django.template import loader
from django.http import HttpResponse
from medico.models import Doctor

def bienvenida(request):
    cantidad_medicos = Doctor.objects.count()
    medicos = Doctor.objects.order_by('apellido','nombre')
    dict_datos = {'cantidad_medicos': cantidad_medicos, 'medicos': medicos}
    pagina = loader.get_template('bienvenida.html')
    return HttpResponse(pagina.render(dict_datos, request))


