# Generated by Django 2.2.6 on 2019-11-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0007_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=255, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
    ]