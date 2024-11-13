import datetime
from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    # managers para el modelo Libros


    # listar libros nadamas por palabras
    def listar_libros(self,kword):
        resultado = self.filter(
            # Busca coincidencias
            titulo__icontains = kword,
            fecha__range=('2000-01-01', '2024-12-01')
            )
        return resultado

    # Listar libros por palabras y fechas
    def listar_libros2(self,kword, fecha1, fecha2):
        
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d")

        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range=(date1, date2)
        )
        return resultado
    
    # Mostrar los libros de la categoria
    def listar_libros_categoria(self,categoria):
        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')
    
    # Agregar un autor al libro atravez del manager
    def add_autor__libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro
    

class CategoriaManager(models.Manager):
    # managers para el modelo categoria

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id = autor
        ).distinct()