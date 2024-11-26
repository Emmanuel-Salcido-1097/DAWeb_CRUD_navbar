from django.urls import  path
from SeguridadPrivada_app import views

urlpatterns = [
    path('seguridadp', views.inicio_vistaSeguridadP, name='seguridadp'),
    path('registrarSeguridadPrivada/', views.registrarSeguridadPrivada, name='registrarSeguridadPrivada'),
    path("seleccionarSeguridadPrivada/<Id_Seguridad>",views.seleccionarSeguridadPrivada,name="seleccionarSeguridadPrivada"),
    path("editarSeguridadPrivada/",views.editarSeguridadPrivada,name="editarSeguridadPrivada"),
    path("borrarSeguridadPrivada/<Id_Seguridad>",views.borrarSeguridadPrivada,name="borrarSeguridadPrivada"),
] 