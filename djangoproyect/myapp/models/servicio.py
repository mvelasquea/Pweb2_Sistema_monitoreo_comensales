from django.db import models
from .Pago import Pago
class servicio(models.Model):
    id_pago=models.ForeignKey(Pago , on_delete=models.CASCADE)
    id_servicio = models.BigAutoField(primary_key=True)
    tipo=models.CharField(max_length=100)
    status =models.BooleanField(default=False)
    fecha = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    status =models.BooleanField(default=False)
    