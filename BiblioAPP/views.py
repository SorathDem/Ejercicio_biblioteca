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
        autor_nombre_icontains=query
    ) | Libro.objects.filter(
        genero__icontains=query
    )
    return render(request, "buscar.html", {"libros": resultados, "query": query})