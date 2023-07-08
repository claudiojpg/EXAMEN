from django.db import models
import uuid



#modelo noticias 

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    id_noticia = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo