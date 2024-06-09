from django.db import models
from .Estudiante import Estudiante

class Asistencia (models.Model):
    Estudiante =models.ForeignKey( Estudiante, on_delete=models.CASCADE)
    id_Asistencia = models.BigAutoField(primary_key=True)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)