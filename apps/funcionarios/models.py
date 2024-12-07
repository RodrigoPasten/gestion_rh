from django.db import models


class Funcionario(models.Model):
    nombre = models.CharField(max_length=100, help_text='Nombre del funcionario')

    def __str__(self):
        return self.nombre
