from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128) 
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.email})'