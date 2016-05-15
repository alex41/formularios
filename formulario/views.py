from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy 
from .models import Registro


class RegistroList(ListView):
	model = Registro 


class RegistroCreate(CreateView):
	model = Registro
	success_url = reverse_lazy('list')
	fields = ['nombres', 'apellidos', 'imagen', 'description']
	



	

