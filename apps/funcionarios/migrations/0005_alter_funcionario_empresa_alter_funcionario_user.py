# Generated by Django 5.1.4 on 2024-12-07 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_alter_empresa_nombre'),
        ('funcionarios', '0004_alter_funcionario_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
