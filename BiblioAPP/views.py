from django.shortcuts import render
from .models import Libro
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Count
from django.utils.timezone import now

# Create your views here.
def principal(request):
    return render(request, "index.html")



def listar_libros(request):
    query = request.GET.get('q', '')
    if query:
        libros = Libro.objects.filter(
            titulo__icontains=query
        ) | Libro.objects.filter(
            autor__nombre__icontains=query
        ) | Libro.objects.filter(
            genero__icontains=query
        )
    else:
        libros = Libro.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('tabla_libros.html', {'libros': libros})
        return HttpResponse(f'<div id="tablaLibros">{html}</div>')

    return render(request, 'libros.html', {'libros': libros, 'query': query})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Autor, Usuario, Prestamo
from .forms import LibroForm, AutorForm, UsuarioForm, PrestamoForm

# Libros
def listar_libros(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda desde la URL
    libros = Libro.objects.all()

    # Si hay un término de búsqueda, filtrar los resultados
    if query:
        libros = libros.filter(titulo__icontains=query)  # Buscar por título (puedes agregar más filtros)

    return render(request, 'lista_libros.html', {'libros': libros, 'query': query})


def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_libros")
    else:
        form = LibroForm()
    return render(request, "formulario.html", {"form": form})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect("lista_libros")
    return render(request, "formulario.html", {"form": form})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    return redirect("lista_libros")

def vista_general(request):
    libros = Libro.objects.all()
    autores = Autor.objects.all()
    usuarios = Usuario.objects.all()
    prestamos = Prestamo.objects.all()
    return render(request, 'lista.html', {
        'libros': libros,
        'autores': autores,
        'usuarios': usuarios,
        'prestamos': prestamos
    })

# Repite lo mismo para Autor, Usuario, Prestamo con sus respectivas vistas y templates.

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'detalle.html', {'libro': libro})

# Editar libro
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'formulario.html', {'form': form})

# Eliminar libro
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'eliminar.html', {'libro': libro})

# Ver autor
def detalle_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'detalle.html', {'autor': autor})

# Editar autor
def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('lista_autores')
    return render(request, 'formulario.html', {'form': form})

# Eliminar autor
def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'eliminar.html', {'autor': autor})

# Ver usuario
def detalle_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'detalle.html', {'usuario': usuario})

# Editar usuario
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, 'formulario.html', {'form': form})

# Eliminar usuario
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'eliminar.html', {'usuario': usuario})

# Ver préstamo
def detalle_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    return render(request, 'detalle.html', {'prestamo': prestamo})

# Editar préstamo
def editar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    form = PrestamoForm(request.POST or None, instance=prestamo)
    if form.is_valid():
        form.save()
        return redirect('lista_prestamos')
    return render(request, 'formulario.html', {'form': form})

# Eliminar préstamo
def eliminar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == "POST":
        prestamo.delete()
        return redirect('lista_prestamos')
    return render(request, 'eliminar.html', {'prestamo': prestamo})

# Lista de préstamos
def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'lista_prestamos.html', {'prestamos': prestamos})

# Crear préstamo
def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'formulario.html', {'form': form})

# Lista de usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

# Crear usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'lista_autores.html', {'autores': autores})

# Crear autor
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'formulario.html', {'form': form})

def marcar_como_devuelto(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    prestamo.devuelto = True
    prestamo.save()
    return redirect('lista_prestamos')

def autor_con_mas_libros(request):
    autor = Autor.objects.annotate(total_libros=Count('libro')).order_by('-total_libros').first()
    return render(request, 'autor_mas_libros.html', {'autor': autor})

def usuarios_con_prestamos_vencidos(request):
    prestamos_vencidos = Prestamo.objects.filter(fecha_devolucion__lt=now().date(), devuelto=False)
    return render(request, 'prestamos_vencidos.html', {'prestamos': prestamos_vencidos})