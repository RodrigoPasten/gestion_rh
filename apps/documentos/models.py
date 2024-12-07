from django.db import models


class Documento(models.Model):
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.descripcion