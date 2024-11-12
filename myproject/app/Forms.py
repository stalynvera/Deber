from django import forms
from .models import Producto,Categoria,Cliente,Orden

class ProductoForm(forms.ModelForm):
    class Meta:
       model = Producto
       fields = ['nombre','descripcion','precio']
 
 # Formulario para Categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

# Formulario para Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']

# Formulario para Orden
class OrdenForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Orden
        fields = ['cliente', 'productos', 'total']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']