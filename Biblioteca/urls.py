"""
URL configuration for Biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django import views
from BiblioAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/index/')),
    path('index/', views.principal, name='principal'),
    path('catalogo/', views.vista_general, name='vista_general'),

   

    # Libros
    path('libros/', views.listar_libros, name='listar_libros'),
    path('libros/nuevo/', views.crear_libro, name='crear_libro'),
    path('libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('libros/<int:pk>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:pk>/eliminar/', views.eliminar_libro, name='eliminar_libro'),

    # Autores
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/nuevo/', views.crear_autor, name='crear_autor'),
    path('autores/<int:pk>/', views.detalle_autor, name='detalle_autor'),
    path('autores/<int:pk>/editar/', views.editar_autor, name='editar_autor'),
    path('autores/<int:pk>/eliminar/', views.eliminar_autor, name='eliminar_autor'),

    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:pk>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

    # Préstamos
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('prestamos/nuevo/', views.crear_prestamo, name='crear_prestamo'),
    path('prestamos/<int:pk>/', views.detalle_prestamo, name='detalle_prestamo'),
    path('prestamos/<int:pk>/editar/', views.editar_prestamo, name='editar_prestamo'),
    path('prestamos/<int:pk>/eliminar/', views.eliminar_prestamo, name='eliminar_prestamo'),
    path('prestamos/<int:prestamo_id>/devolver/', views.marcar_como_devuelto, name='marcar_como_devuelto'),
    path('autor/mas-libros/', views.autor_con_mas_libros, name='autor_con_mas_libros'),
    path('prestamos/vencidos/', views.usuarios_con_prestamos_vencidos, name='usuarios_con_prestamos_vencidos'),

]


