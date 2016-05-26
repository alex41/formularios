from __future__ import unicode_literals

from django.db import models

class Registro(models.Model):

	nombres  = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	#comentarios = models.CharField(max_length = 50,widget = forms.Textare)
	#imagen = models.ImageField(blank=True) 
	#description = models.TextField()

	#picture = models.ImageField(blank=True)

