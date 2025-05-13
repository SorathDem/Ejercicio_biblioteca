from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField() 

    def __str__(self):
        return f'{self.libro} prestado a {self.usuario}'
                                        
            