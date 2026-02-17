from django.shortcuts import render
from administracion.models import Libro, Prestamo
# Create your views here.
def bienvenida(request):
    total_libros = Libro.objects.count()
    total_prestamos = Prestamo.objects.count()
    total_usuarios = Prestamo.objects.values('usuario').distinct().count()  # usuarios únicos

    contexto = {
        'total_libros': total_libros,
        'total_prestamos': total_prestamos,
        'total_usuarios': total_usuarios,
    }

    return render(request, 'sistema/bienvenida.html', contexto)




