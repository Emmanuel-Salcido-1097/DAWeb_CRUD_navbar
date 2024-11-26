from django.shortcuts import render, redirect
from .models import Socios

# Create your views here.

def inicio_vistaSocios(request):
    socios = Socios.objects.all()
    return render(request, 'gestionarSocios.html', {'socios': socios})

def registrarSocios(request):
    Id_Socio =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    tipo_socio = request.POST['txtts']
    contacto = request.POST['txtcontacto']
    email = request.POST['email']
    aporte = request.POST['txtaporte']
    beneficio = request.POST['txtbeneficio']
    
    guardarSo = Socios.objects.create(Id_Socio=Id_Socio, nombre=nombre, tipo_socio=tipo_socio,
                                                    contacto=contacto, email=email, aporte=aporte, beneficio=beneficio)
    return redirect('socios')

def seleccionarSocios( request, Id_Socio):
    socios = Socios.objects.get(Id_Socio=Id_Socio)
    return render(request, 'editarSocios.html', {'socios': socios})

def editarSocios(request):
    Id_Socio =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    tipo_socio = request.POST['txtts']
    contacto = request.POST['txtcontacto']
    email = request.POST['email']
    aporte = request.POST['txtaporte']
    beneficio = request.POST['txtbeneficio']
    
    socios = Socios.objects.get(Id_Socio=Id_Socio)
    socios.nombre = nombre
    socios.tipo_socio = tipo_socio
    socios.contacto = contacto
    socios.email = email
    socios.aporte = aporte
    socios.beneficio = beneficio 
    socios.save()
    return redirect('socios')

def borrarSocios(request,Id_Socio):
    socios=Socios.objects.get(Id_Socio=Id_Socio)
    socios.delete()
    return redirect("socios")