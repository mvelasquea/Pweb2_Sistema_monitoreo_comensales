from django.db import models
from .Asistencia import Asistencia

class FaltaAsistencia (models.Model):
    Asistencia =models.ForeignKey( Asistencia, on_delete=models.CASCADE)
    id_FaltaAsistencia = models.BigAutoField(primary_key=True)
    fecha = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)