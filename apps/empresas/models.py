from django.db import models


class Empresa(models.Model):
    nombre = models.CharField(max_length=100, help_text='nombre empresa')
