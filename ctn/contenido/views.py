# Create your views here.
from contenido.models import *
from django.shortcuts import render_to_response
from django import forms
from django.shortcuts import render_to_response

def municipio(request):
    bbdd = Municipio.objects.all()
    bbdd2 = Senderos.objects.all()
    senderos = []
    municipio = []

    for i in bbdd:
        municipio.append(i)

    for i in bbdd2:
        senderos.append(i)

    context = {'municipio':municipio, 'senderos':senderos}
    return render_to_response('senderos/senderos.html', context)

def municipio2(request):
    bbdd = Municipio.objects.all()
    municipio2 = []

    for i in bbdd:
        municipio2.append(i)

    context = {'municipio2':municipio2,}
    return render_to_response('municipios/municipios.html', context)

def municipio3(request, n_municipio):
    
    municipio = Municipio.objects.get(id=n_municipio)
    nid = n_municipio
    nombre = municipio.Nombre
    latitud = municipio.Latitud
    longitud = municipio.Longitud
    telefono = municipio.TlfA

    context = {'nid':nid,'nombre':nombre, 'latitud':latitud, 'longitud':longitud, 'tlfa':telefono,}
    
    return render_to_response('municipios/municipios_info.html', context)
    
def senderos(request, n_sendero):
    
    sendero = Senderos.objects.get(id=n_sendero)
    nid = n_sendero
    nombre = sendero.Nombre
    latitud = sendero.Latitud
    longitud = sendero.Longitud
    municipio = sendero.MuNom
    puntos = sendero.Puntuacion
    aux = sendero.Coordenadas.split(',')
    coordenadas = []
    for i in aux:
        coordenadas.append(float(i))
    print len(coordenadas)
    

    context = {'nid':nid,'nombre':nombre, 'latitud':latitud, 'longitud':longitud, 'municipio':municipio, 'puntos':puntos, 'coordenadas':coordenadas}
    
    return render_to_response('senderos/senderos_info.html', context)