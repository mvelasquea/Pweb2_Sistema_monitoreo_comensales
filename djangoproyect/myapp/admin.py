from django.contrib import admin

from .models.Estudiante import Estudiante
from .models.Pago import Pago
from .models.servicio import servicio
from .models.FaltaPago import FaltaPago
from .models.Asistencia import Asistencia
from .models.FaltaAsistencia import FaltaAsistencia
from .models.Justificacion import Justificacion

admin.site.register(Estudiante)
admin.site.register(Pago)
admin.site.register(FaltaPago)
admin.site.register(servicio)
admin.site.register(Asistencia)
admin.site.register(FaltaAsistencia)
admin.site.register(Justificacion)
# Register your models here.
