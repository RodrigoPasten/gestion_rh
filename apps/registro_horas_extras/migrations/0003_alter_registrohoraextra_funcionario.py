# Generated by Django 5.1.4 on 2024-12-07 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_alter_funcionario_empresa_alter_funcionario_user'),
        ('registro_horas_extras', '0002_registrohoraextra_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.funcionario'),
        ),
    ]