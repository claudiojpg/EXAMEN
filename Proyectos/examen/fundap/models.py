from django.db import models

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class paciente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    Informacion_salud = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()
  
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)

    class Meta:      
        ordering = ['rut']


class medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre