# Create your views here.
from contenido.models import *
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
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
    
    sendero = Senderos.objects.get(id=nid)
    resultado = sendero.puntos/sendero.NVotos
    print resultado
    if resultado == 1:
        mensaje = 'No Recomendado'
    elif resultado == 2:
        mensaje = 'Regular'
    elif resultado == 3:
        mensaje = 'Bien'
    else :
        mensaje = 'Muy Bien' 



    context = {'mensaje':mensaje,'nid':nid,'nombre':nombre, 'latitud':latitud, 'longitud':longitud, 'municipio':municipio, 'puntos':puntos, 'coordenadas':coordenadas}
    
    return render_to_response('senderos/senderos_info.html', context)


def votos(request, voto, sid):
        
    voto = int(voto)
    sendero = Senderos.objects.get(id=sid)
    sendero.puntos = voto+sendero.puntos
    sendero.NVotos = 1 + sendero.NVotos
    

    print sendero.puntos
    print sendero.NVotos
    sendero.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))