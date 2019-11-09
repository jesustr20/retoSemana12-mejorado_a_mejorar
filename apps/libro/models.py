from django.db import models


# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha Publicación', blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='media/%d', blank=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha Publicación', blank=False, null=False)
    libro_id = models.ManyToManyField(Libro)
    autor_id = models.ManyToManyField(Autor)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=255, blank=False, null=False)
    apellido = models.CharField('Apellido', max_length=255, blank=False, null=False)
    fecha_registro = models.DateField('Fecha Registro', blank=False, null=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} {self.fecha_registro}'

class Alquiler(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_id = models.ManyToManyField(Cliente)
    libro_id = models.ManyToManyField(Libro)
    fecha_Alquiler = models.DateField('Fecha Alquiler', auto_now=True, auto_now_add=False)
    fecha_devolucion = models.DateField('Fecha Devolución', blank=False, null=False)

    class Meta:
        verbose_name = 'Alquiler'
        verbose_name_plural = 'Alquileres'
        ordering = ['fecha_Alquiler']

    def __str__(self):
        return self.fecha_devolucion