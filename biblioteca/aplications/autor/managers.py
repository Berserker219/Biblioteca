from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    # managers para el modelo autor

    def buscar_autor(self,kword):
        resultado = self.filter(
            # Busca coincidencias
            nombre__icontains = kword
            )
        return resultado
    
    def buscar_autor2(self,kword):
        resultado = self.filter(
            # "o"
            Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)
            )
        return resultado
    
    def buscar_autor3(self,kword):

        resultado = self.filter(
            # excluir
            nombre__icontains = kword
            ).exclude(
                Q(edad__icontains = 35) | Q(apellidos__icontains = 65)
            )
        return resultado

    def buscar_autor4(self,kword):
        resultado = self.filter(
            # 'y'
            edad_gt=40,
            edad_lt=65
            ).order_by('apellidor', 'nombre', 'id') # Ordernar
            
        return resultado