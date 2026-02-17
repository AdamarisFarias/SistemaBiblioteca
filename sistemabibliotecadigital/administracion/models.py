from django.db import models
# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20, unique=True)
    categoria = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    cantidad_disponible = models.PositiveIntegerField()
    editorial = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Prestamo(models.Model):
    ESTADO_CHOICES = [
        ('prestado', 'Prestado'),
        ('devuelto', 'Devuelto'),
        ('atrasado', 'Atrasado')
    ]

    usuario = models.CharField(max_length=150)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"{self.libro.titulo} - {self.usuario}"
