from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=70, help_text='Nombre de departamento')

    def __str__(self):
        return self.nombre
