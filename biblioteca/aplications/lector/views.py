# python
from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
# modelos
from .models import Prestamo
# formularios
from .forms import PrestamoForm, MultiplePrestamoForm

class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):

        # create crea una nueva instancia, genera un nuevo id ( insert)
        #Prestamo.objects.create(
        #    lector = form.cleaned_data['lector'],
        #    libro = form.cleaned_data['libro'],
        #    fecha_prestamo = date.today(),
        #    devuelto = False
        #)

        # save actualiza y sobreescribe todos los datos, si no esta lo create ( update)
        prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False
        )
        prestamo.save()

        libro = form.cleaned_data['libro']
        libro.stok = libro.stok - 1 # quitando el stok
        libro.visitas = libro.visitas + 1 # aumento de vistas
        libro.save()


        return super(RegistrarPrestamo,self).form_valid(form)
    


class ADDPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):

        # validacion de existencia
        obj, created = Prestamo.objects.get_or_create(
            lector =  form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            # En caso de que no encuentre el registro dentro del modelo prestamo lo vas a crear
            defaults= {
                'fecha_prestamo': date.today()
            } 
        )

        # si no hay registro se crea, si hay registro lo redirige
        if created:
            return super(ADDPrestamo,self).form_valid(form)
        else:
            return HttpResponseRedirect('/')
        


class ADDMultiplePrestamo(FormView):
    template_name = 'lector/add_multiple_prestamo.html'
    form_class = MultiplePrestamoForm
    success_url = '.'

    def form_valid(self, form):

        prestamos = []

        for l in form.cleaned_data['libros']:
            obj, created = Prestamo.objects.get_or_create(
                lector = form.cleaned_data['lector'],
                libro = l,
                fecha_prestamo = date.today(),
                devuelto = False,
                defaults={
                    'fecha_prestamo': date.today()
                }
            )
            if created:
                prestamos.append(obj)
        
        # crear registros dentro de modelo prestamos a partir de una lista, registra todo en una sola consulta
        
        if prestamos:
            Prestamo.objects.bulk_create(
                prestamos, ignore_conflicts=True
            ) 
        return super(ADDMultiplePrestamo, self).form_valid(form) if prestamos else HttpResponseRedirect(self.success_url)

        


        