from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Prestamo
from .forms import LibroForm, PrestamoForm
# Create your views here.
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'administracion/libros/lista.html', {'libros': libros})

def crear_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'administracion/libros/form.html', {'form': form})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'administracion/libros/form.html', {'form': form})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'administracion/libros/eliminar.html', {'libro': libro})

def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'administracion/prestamos/lista.html', {'prestamos': prestamos})

def crear_prestamo(request):
    form = PrestamoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_prestamos')
    return render(request, 'administracion/prestamos/form.html', {'form': form})

def editar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)
    form = PrestamoForm(request.POST or None, instance=prestamo)
    if form.is_valid():
        form.save()
        return redirect('lista_prestamos')
    return render(request, 'administracion/prestamos/form.html', {'form': form})

def eliminar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('lista_prestamos')
    return render(request, 'administracion/prestamos/eliminar.html', {'prestamo': prestamo})
