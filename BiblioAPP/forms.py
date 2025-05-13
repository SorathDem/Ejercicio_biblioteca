from django import forms
from .models import Libro, Autor, Usuario, Prestamo


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__' 


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }