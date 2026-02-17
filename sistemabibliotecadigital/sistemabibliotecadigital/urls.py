"""
URL configuration for sistemabibliotecadigital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema.views import bienvenida
from administracion.views import (
    lista_libros, crear_libro, editar_libro, eliminar_libro,
    lista_prestamos, crear_prestamo, editar_prestamo, eliminar_prestamo
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida, name='bienvenida'),
    path('libros/', lista_libros, name='lista_libros'),
    path('libros/crear/', crear_libro, name='crear_libro'),
    path('libros/editar/<int:id>/', editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:id>/', eliminar_libro, name='eliminar_libro'),
    path('prestamos/', lista_prestamos, name='lista_prestamos'),
    path('prestamos/crear/', crear_prestamo, name='crear_prestamo'),
    path('prestamos/editar/<int:id>/', editar_prestamo, name='editar_prestamo'),
    path('prestamos/eliminar/<int:id>/', eliminar_prestamo, name='eliminar_prestamo')
]





