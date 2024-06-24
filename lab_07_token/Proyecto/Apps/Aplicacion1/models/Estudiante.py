from django.db import models

class Estudiante(models.Model):
    id_Estudiante = models.BigAutoField(primary_key=True)
    nombre =models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    carrera=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    
