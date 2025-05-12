from django import forms
from .models import Libro, Autor, Usuario, Prestamo

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '_all_'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '_all_'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '_all_'

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '_all_'