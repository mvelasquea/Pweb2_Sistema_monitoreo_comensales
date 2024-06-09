from django.db import models
from .FaltaAsistencia import FaltaAsistencia

class Justificacion (models.Model):
    FaltaAsistencia =models.ForeignKey( FaltaAsistencia, on_delete=models.CASCADE)
    id_justificacion = models.BigAutoField(primary_key=True)
    descripcion=models.TextField()
    fecha = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)