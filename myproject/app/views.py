from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto
from .Forms import ProductoForm

# Crear
@login_required
@permission_required('app.add_producto', raise_exception=True)
def producto_crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm()
    
    return render(request, 'app/producto_form.html', {'form': form})

# Leer
@login_required
@permission_required('app.view_producto', raise_exception=True)
def producto_lista(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'app/producto_lista.html', {'productos': productos})

# Vista para editar el producto
@login_required
@permission_required('app.change_producto', raise_exception=True)
def producto_editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_editar_lista')  # Redirige de vuelta a la lista de productos después de editar
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'app/producto_editar.html', {'form': form, 'producto': producto})

# Eliminar
@login_required
@permission_required('app.delete_producto', raise_exception=True)
def producto_eliminar(request):
    productos = Producto.objects.all()  # Obtén todos los productos

    # Si se envía una solicitud POST, se eliminará el producto correspondiente
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        if producto_id:
            producto = get_object_or_404(Producto, id=producto_id)
            producto.delete()  # Elimina el producto
            return redirect('producto_eliminar')  # Redirige a la misma página para actualizar la lista

    return render(request, 'app/producto_eliminar.html', {'productos': productos})

# Vista que lista todos los productos con un botón para editar cada uno
@login_required
@permission_required('app.view_producto', raise_exception=True)
def producto_editar_lista(request):
    productos = Producto.objects.all()
    return render(request, 'app/producto_editar_lista.html', {'productos': productos})
