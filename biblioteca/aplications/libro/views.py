from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView

# models local
from .models import Libro

# Create your views here.



class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        f1 = self.request.GET.get('fecha1', '')
        f2 = self.request.GET.get('fecha2', '')

        if f1 and f2:
            return Libro.objects.listar_libros2(palabra_clave, f1, f2)
        else:
            return Libro.objects.listar_libros(palabra_clave)
        

class ListLibrosTrg(ListView):
    context_object_name = 'lista_libros_trg'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        return Libro.objects.listar_libros_trg(palabra_clave)
        


# Libros de la misma categoria
class ListLibros2(ListView):
    context_object_name = 'lista_libros2'
    template_name = "libro/lista2.html"

    def get_queryset(self):
        
        return Libro.objects.listar_libros_categoria('4')
    
# Detalle del libro
class LibroDetailView(DetailView):
    template_name = 'Libro/detalle.html'
    model = Libro