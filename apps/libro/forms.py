from django import forms
from .models import Autor, Libro, Editorial, Cliente, Alquiler


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor_id','fecha_publicacion', 'image']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'libro_id', 'autor_id', 'fecha_publicacion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'fecha_registro']

class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['cliente_id', 'libro_id', 'fecha_devolucion']