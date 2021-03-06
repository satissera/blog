from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada, Mensajes
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage
import json

# Create your views here.
def home(request):
	context = RequestContext(request)
	posts = Entrada.objects.all()
	return render_to_response('SitioWebHoshible.html',{'posts':posts}, context)

def contacto (request):
	context = RequestContext(request)
	if request.method == 'POST':
		nombre = request.POST['nombre']
		asunto = request.POST['asunto']
		mail = request.POST['mail']
		mensaje= request.POST['mensaje']
		email = EmailMessage(asunto, 'Nombre: '+nombre+"\n"+'Mail: '+mail+"\n\n"+mensaje, to=['piojotissera@gmail.com'])
		#email = EmailMessage(asunto, 'Nombre: '+nombre, to=['piojotissera@gmail.com'])
		email.send()        
	return render_to_response('Contactos.html', context)

def conversor (request):
	context = RequestContext(request)
	return render_to_response('CambioDeMoneda.html', context)

def calcu (request):
	context = RequestContext(request)
	return render_to_response('Calcu.html', context)

def crono (request):
	context = RequestContext(request)
	return render_to_response('Cronometro1.html', context)

def curriculum (request):
	context = RequestContext(request)
	return render_to_response('Curriculum.html', context)

def ver_post(request, id_post):
	context = RequestContext(request)
	mi_post = Entrada.objects.get(id=id_post)
	mensajes = Mensajes.objects.filter(published_in = mi_post, published = True) 
	return render_to_response('post.html', {'post':mi_post,'mensajes':mensajes},context)
	
def comentar(request):
	if request.method == 'POST':
		context = RequestContext(request)      
        	nombre = request.POST['nombre']
        	mensaje = request.POST['mensaje']   
        	id_post = request.POST['id']
        	comentario = Mensajes()
        	comentario.mensaje = mensaje        
        	comentario.nombre = nombre
        	comentario.published_in = Entrada.objects.get(id=id_post)
        	comentario.save()
        	comentarioReturn = {"nombre": comentario.nombre, "fecha": "Ahora", "mensaje":comentario.mensaje}
    		return HttpResponse(json.dumps(comentarioReturn), content_type="application/json")
	return


			
	




