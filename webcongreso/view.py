'''
Created on 05/05/2013

@author: ever
'''
from django.shortcuts import render_to_response
from django.template import RequestContext

# para poder enviar los css en /static/ se pone el ultimo parametro
def web(request):
    titulo = 'Bienvenido a la web del congreso'
    return render_to_response('index.html', {'title': titulo},context_instance=RequestContext(request))

def presentacion(request):
    return render_to_response('presentacion.html',context_instance=RequestContext(request))

def cronograma(request):
    return render_to_response('cronograma.html',context_instance=RequestContext(request))

def mision_vision(request):
    return render_to_response('mision_vision.html',context_instance=RequestContext(request))

def comision_organizadora(request):
    return render_to_response('comision_organizadora.html',context_instance=RequestContext(request))

def costos_vida(request):
    return render_to_response('costos_vida.html',context_instance=RequestContext(request))

def contactenos(request):
    return render_to_response('contactenos.html',context_instance=RequestContext(request))

def papers(request):
    return render_to_response('papers.html',context_instance=RequestContext(request))
