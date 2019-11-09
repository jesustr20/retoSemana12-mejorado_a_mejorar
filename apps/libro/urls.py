from django.urls import path
from .views import crear_autor, listar_autores, editar_autor, eliminar_autor
from .views import libro_crear, libro_listar, libro_editar, libro_eliminar
from .views import editorial_crear, editorial_listar, editorial_editar, editorial_eliminar
from .views import cliente_crear, cliente_listar, cliente_editar, cliente_eliminar
from .views import alquiler_crear, alquiler_listar, alquiler_editar, alquiler_eliminar

urlpatterns = [
    #Autor
    path('listar_autores/', listar_autores, name='listar_autores'),
    path('crear_autor/', crear_autor, name='crear_autor'),
    path('editar_autor/<int:autor_id>', editar_autor, name='editar_autor'),
    path('eliminar_autor/<int:autor_id>', eliminar_autor, name='eliminar_autor'),

    #Libro
    path('libro_crear/', libro_crear, name='libro_crear'),
    path('libro_listar/', libro_listar, name='libro_listar'),
    path('libro_editar/<int:libro_id>', libro_editar, name='libro_editar'),
    path('libro_eliminar/<int:libro_id>', libro_eliminar, name='libro_eliminar'),

    #Editorial
    path('editorial_crear/', editorial_crear, name='editorial_crear'),
    path('editorial_listar/', editorial_listar, name='editorial_listar'),
    path('editorial_editar/<int:edito_id>', editorial_editar, name='editorial_editar'),
    path('editorial_eliminar/<int:edito_id>', editorial_eliminar, name='editorial_eliminar'),

    #Cliente
    path('cliente_crear/', cliente_crear, name='cliente_crear'),
    path('cliente_listar/', cliente_listar, name='cliente_listar'),
    path('cliente_editar/<int:cli_id>', cliente_editar, name='cliente_editar'),
    path('cliente_eliminar/<int:cli_id>', cliente_eliminar, name='cliente_eliminar'),

    #Alquiler
    path('alquiler_crear/', alquiler_crear, name='alquiler_crear'),
    path('alquiler_listar/', alquiler_listar, name='alquiler_listar'),
    path('alquiler_editar/<int:alqui_id>', alquiler_editar, name='alquiler_editar'),
    path('alquiler_eliminar/<int:alqui_id>', alquiler_eliminar, name='alquiler_eliminar')
]
