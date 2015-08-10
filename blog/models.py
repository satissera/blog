# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Entrada(models.Model):
	class Meta:
		verbose_name = "Mi Entrada"
		verbose_name_plural = "Todas mis entradas"
		ordering=['-fecha']

	titulo = models.CharField(u'Título', max_length=100)
	fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
	resumen= models.CharField(u'Resumen',max_length=512)
	contenido = models.TextField(u'Contenido')

	def __str__(self):
		return self.titulo


class Mensajes(models.Model):
	class Meta:
		verbose_name = "Mensaje"
		verbose_name_plural = "Todos los mensajes"
		ordering=['-fecha']
	nombre= models.CharField(u'Nombre', max_length=70)
	fecha = models.DateTimeField(u'Fecha del comentario',auto_now_add=True)
	published = models.BooleanField(u'Publicado?', default=True)
	mensaje= models.TextField(u'Mensaje')
	published_in = models.ForeignKey(Entrada)
	def __str__(self):
		return self.nombre
