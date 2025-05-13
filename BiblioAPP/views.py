from django.shortcuts import render
from .models import Libro

# Create your views here.
def principal(request):
    return render(request, "index.html")



def buscar_libros(request):
    query = request.GET.get("q", "")
    resultados = Libro.objects.filter(
        titulo__icontains=query
    ) | Libro.objects.filter(
        autor__nombre__icontains=query
    ) | Libro.objects.filter(
        genero__icontains=query
    )
    return render(request, "buscar.html", {"libros": resultados, "query": query})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Autor, Usuario, Prestamo
from .forms import LibroForm, AutorForm, UsuarioForm, PrestamoForm

# Libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "lista.html", {"libros": libros})

def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_libros")
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

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, "libros/lista.html", {
        "objetos": libros,
        "titulo": "Libros",
        "crear_url": "crear_libro",
        "editar_url": "editar_libro",
        "eliminar_url": "eliminar_libro",
    })
# Repite lo mismo para Autor, Usuario, Prestamo con sus respectivas vistas y templates.

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle.html', {'libro': libro})

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
    return render(request, 'libros/eliminar.html', {'libro': libro})

# Ver autor
def detalle_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'autores/detalle.html', {'autor': autor})

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
    return render(request, 'autores/eliminar.html', {'autor': autor})