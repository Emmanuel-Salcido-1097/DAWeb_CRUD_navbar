from django.urls import  path
from Socios_app import views

urlpatterns = [
    path('socios', views.inicio_vistaSocios, name='socios'),
    path('registrarSocios/', views.registrarSocios, name='registrarSocios'),
    path("seleccionarSocios/<Id_Socio>",views.seleccionarSocios,name="seleccionarSocios"),
    path("editarSocios/",views.editarSocios,name="editarSocios"),
    path("borrarSocios/<Id_Socio>",views.borrarSocios,name="borrarSocios"),
] 