from django.shortcuts import render, redirect
from .models import Servicios

# Create your views here.

def inicio_vistaServicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'gestionarServicios.html', {'servicios': servicios})

def registrarServicios(request):
    Id_Servicio =  request.POST['txtid']
    Id_cliente =  request.POST['txtidc']
    Id_Empleado = request.POST['txtide']
    tipo = request.POST['txttipo']
    encargado = request.POST['txtencargado']
    transferencia = request.POST['txttransferencia']
    deposito = request.POST['txtdeposito']
    fecha_serv = request.POST['txtfecha']
     
    guardarSe = Servicios.objects.create(Id_Servicio=Id_Servicio, Id_cliente=Id_cliente, Id_Empleado=Id_Empleado,
                                                tipo=tipo, encargado=encargado, transferencia=transferencia, 
                                                    deposito=deposito, fecha_serv=fecha_serv)
    return redirect('servicios')

def seleccionarServicios( request, Id_Servicio):
    servicios = Servicios.objects.get(Id_Servicio=Id_Servicio)
    return render(request, 'editarServicios.html', {'servicios': servicios})

def editarServicios(request):
    Id_Servicio =  request.POST['txtid']
    Id_cliente =  request.POST['txtidc']
    Id_Empleado = request.POST['txtide']
    tipo = request.POST['txttipo']
    encargado = request.POST['txtencargado']
    transferencia = request.POST['txttransferencia']
    deposito = request.POST['txtdeposito']
    fecha_serv = request.POST['txtfecha']
    
    servicios = Servicios.objects.get(Id_Servicio=Id_Servicio)
    servicios.Id_cliente = Id_cliente
    servicios.Id_Empleado = Id_Empleado
    servicios.tipo = tipo
    servicios.encargado = encargado
    servicios.transferencia = transferencia
    servicios.deposito = deposito 
    servicios.fecha_serv = fecha_serv
    servicios.save()
    return redirect('servicios')

def borrarServicios(request,Id_Servicio):
    servicios=Servicios.objects.get(Id_Servicio=Id_Servicio)
    servicios.delete()
    return redirect("servicios")