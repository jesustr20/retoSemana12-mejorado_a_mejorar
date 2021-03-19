# Generated by Django 2.2.6 on 2019-11-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_libro_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Titulo')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha Publicación')),
                ('autor_id', models.ManyToManyField(to='libro.Autor')),
                ('libro_id', models.ManyToManyField(to='libro.Libro')),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editoriales',
                'ordering': ['nombre'],
            },
        ),
    ]