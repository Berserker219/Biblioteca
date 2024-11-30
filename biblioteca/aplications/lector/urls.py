from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('prestamo/add/', views.ADDPrestamo.as_view(),name='prestamo-add'),
    path('prestamo/multiple-add/', views.ADDMultiplePrestamo.as_view(),name='prestamo_add_multiple'),
]
