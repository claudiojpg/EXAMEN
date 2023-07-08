from django.contrib import admin
from .models import paciente,Genero,medicamento

admin.site.register(Genero)
admin.site.register(paciente)
admin.site.register(medicamento)

# Register your models here.
