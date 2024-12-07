from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text='Ingrese el motivo del las horas extras')

    def __str__(self):
        return self.motivo
