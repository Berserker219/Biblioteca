from django.shortcuts import render
from django.views.generic import ListView

# models local
from .models import Autor

# Create your views here.



class ListAutores(ListView):
    model = Autor
    context_object_name = 'lista_autores'
    template_name = "autor/lista.html"
