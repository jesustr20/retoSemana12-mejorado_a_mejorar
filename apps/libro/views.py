from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import AutorForm, LibroForm, EditorialForm, ClienteForm, AlquilerForm
from .models import Autor, Libro, Editorial, Cliente, Alquiler


# Create your views here.
def home(request):
    return render(request, 'libro/index.html')

#AUTOR
@require_http_methods(["POST", "GET"])
def crear_autor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('/libro/listar_autores')
    else:
        autor_form = AutorForm()

    return render(request, 'libro/crear_autor.html', {
        'autor_form': autor_form
    })


@require_http_methods(["POST", "GET"])
def editar_autor(request, autor_id):
    instancia = Autor.objects.get(id = autor_id)
    if request.method == 'GET':
        autor_form = AutorForm(instance=instancia)
    else:
        autor_form = AutorForm(request.POST, instance=instancia)
        if autor_form.is_valid():
            autor_form.save()
        return redirect('/libro/listar_autores')

    return render(request, 'libro/editar_autor.html', {
        'autor_form': autor_form
    })


@require_http_methods(['GET'])
def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'libro/listar_autor.html', {
        'autores': autores
    })


@require_http_methods(["POST", "GET"])
def eliminar_autor(request, autor_id):
    autores = Autor.objects.get(id = autor_id)
    if request.method == 'POST':
        autores.delete()
        return redirect('/libro/listar_autores')

    return render(request, 'libro/eliminar_autor.html',{
        'autores': autores
    })


#Libro
@require_http_methods(["POST", "GET"])
def libro_crear(request):
    if request.method == 'POST':
        libro_form = LibroForm(request.POST, request.FILES)
        if libro_form.is_valid():
            libro_form.save()
            return redirect('/libro/libro_listar')
    else:
        libro_form = LibroForm()

    return render(request, 'libro/libro_crear.html', {
        'libro_form': libro_form
    })

@require_http_methods(["POST", "GET"])
def libro_editar(request, libro_id):
    instancia = Libro.objects.get(id = libro_id)
    if request.method == 'GET':
        libro_form = LibroForm(instance=instancia)
    else:
        libro_form = LibroForm(request.POST,request.FILES, instance=instancia)
        if libro_form.is_valid():
            libro_form.save()
        return redirect('/libro/libro_listar')

    return render(request, 'libro/libro_editar.html', {
        'libro_form': libro_form
    })

@require_http_methods(['GET'])
def libro_listar(request):
    libros = Libro.objects.all()
    return render(request, 'libro/libro_listar.html', {
        'libros': libros
    })

@require_http_methods(["POST", "GET"])
def libro_eliminar(request, libro_id):
    libro = Libro.objects.get(id = libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('/libro/libro_listar')

    return render(request, 'libro/libro_eliminar.html',{
        'libro': libro
    })


#Editorial
@require_http_methods(["POST", "GET"])
def editorial_crear(request):
    if request.method == 'POST':
        editorial_form = EditorialForm(request.POST)
        if editorial_form.is_valid():
            editorial_form.save()
            return redirect('/libro/editorial_listar')
    else:
        editorial_form = EditorialForm()

    return render(request, 'libro/editorial_crear.html', {
        'editorial_form': editorial_form
    })

@require_http_methods(['GET'])
def editorial_listar(request):
    editoriales = Editorial.objects.all()
    return render(request, 'libro/editorial_listar.html', {
        'editoriales': editoriales
    })

@require_http_methods(["POST", "GET"])
def editorial_editar(request, edito_id):
    instancia = Editorial.objects.get(id = edito_id)
    if request.method == 'GET':
        editorial_form = EditorialForm(instance=instancia)
    else:
        editorial_form = EditorialForm(request.POST, instance=instancia)
        if editorial_form.is_valid():
            editorial_form.save()
        return redirect('/libro/editorial_listar')

    return render(request, 'libro/editorial_editar.html', {
        'editorial_form': editorial_form
    })

@require_http_methods(["POST", "GET"])
def editorial_eliminar(request, edito_id):
    editorial = Editorial.objects.get(id = edito_id)
    if request.method == 'POST':
        editorial.delete()
        return redirect('/libro/editorial_listar')

    return render(request, 'libro/editorial_eliminar.html',{
        'editorial': editorial
    })


#CLIENTE
@require_http_methods(["POST", "GET"])
def cliente_crear(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, request.FILE)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('/libro/cliente_listar')
    else:
        cliente_form = ClienteForm()

    return render(request, 'libro/cliente_crear.html', {
        'cliente_form': cliente_form
    })

@require_http_methods(['GET'])
def cliente_listar(request):
    clientes = Cliente.objects.all()
    return render(request, 'libro/cliente_listar.html', {
        'clientes': clientes
    })

@require_http_methods(["POST", "GET"])
def cliente_editar(request, cli_id):
    instancia = Cliente.objects.get(id = cli_id)
    if request.method == 'GET':
        cliente_form = ClienteForm(instance=instancia)
    else:
        cliente_form = ClienteForm(request.POST, instance=instancia)
        if cliente_form.is_valid():
            cliente_form.save()
        return redirect('/libro/cliente_listar')

    return render(request, 'libro/cliente_editar.html', {
        'cliente_form': cliente_form
    })

@require_http_methods(["POST", "GET"])
def cliente_eliminar(request, cli_id):
    clientes = Cliente.objects.get(id = cli_id)
    if request.method == 'POST':
        clientes.delete()
        return redirect('/libro/cliente_listar')

    return render(request, 'libro/cliente_eliminar.html',{
        'clientes': clientes
    })


#ALQUILER
@require_http_methods(["POST", "GET"])
def alquiler_crear(request):
    if request.method == 'POST':
        alquiler_form = AlquilerForm(request.POST)
        if alquiler_form.is_valid():
            alquiler_form.save()
            return redirect('/libro/alquiler_listar')
    else:
        alquiler_form = AlquilerForm()

    return render(request, 'libro/alquiler_crear.html', {
        'alquiler_form': alquiler_form
    })

@require_http_methods(['GET'])
def alquiler_listar(request):
    alquileres = Alquiler.objects.all()
    return render(request, 'libro/alquiler_listar.html', {
        'alquileres': alquileres
    })

@require_http_methods(["POST", "GET"])
def alquiler_editar(request, alqui_id):
    instancia = Alquiler.objects.get(id = alqui_id)
    if request.method == 'GET':
        alquiler_form = AlquilerForm(instance=instancia)
    else:
        alquiler_form = AlquilerForm(request.POST, instance=instancia)
        if alquiler_form.is_valid():
            alquiler_form.save()
        return redirect('/libro/alquiler_listar')

    return render(request, 'libro/alquiler_editar.html', {
        'alquiler_form': alquiler_form
    })

@require_http_methods(["POST", "GET"])
def alquiler_eliminar(request, alqui_id):
    alquileres = Alquiler.objects.get(id = alqui_id)
    if request.method == 'POST':
        alquileres.delete()
        return redirect('/libro/alquiler_listar')

    return render(request, 'libro/alquiler_eliminar.html',{
        'alquileres': alquileres
    })