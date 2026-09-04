from django.db import models

class ReporteGestion(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Create your models here.
