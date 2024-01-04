"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp.views import bienvenida
from rest_framework import routers

from medico.views import agregar_medico, ver_medico, modificar_medico, eliminar_medico, generar_reporte, \
    PacienteViewSet, DoctorViewSet, CitaViewSet

router = routers.DefaultRouter()
router.register(r'api_paciente', PacienteViewSet)
router.register(r'api_doctor', DoctorViewSet)
router.register(r'api_cita', CitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida, name='inicio'),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('agregar_medico/', agregar_medico),
    path('ver_medico/<int:id>', ver_medico),
    path('modificar_medico/<int:id>', modificar_medico),
    path('eliminar_medico/<int:id>', eliminar_medico),
    path('generar_reporte/', generar_reporte),
]

urlpatterns += router.urls