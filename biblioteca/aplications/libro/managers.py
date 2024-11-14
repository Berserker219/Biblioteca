import datetime
from django.db import models
from django.db.models import Q, Count

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
    
    # numero de veces que fue prestasdos los libros en total
    def libros_num_prestamos(self):
        # aggregate nos devolvera un diccionario, se usa para operaciones
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado

    
    # numeros de veces que fueron prestados cada libro
    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados=Count('libro_prestamo')
        )
        for r in resultado:
            print('===========')
            print(r,r.num_prestados)
        
        return resultado


class CategoriaManager(models.Manager):
    # managers para el modelo categoria

    # Listar las categorias en las que esta cada autor
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id = autor
        ).distinct()
    
    # mostrar cuantos libros hay en cada categoria
    def listar_categoria_libros(self):
        # contar los elementos de la categoria
        # annotate nos devolvera una consulta
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )
        for r in resultado:
            print('*********')
            print(r, r.num_libros)
        return resultado
    
