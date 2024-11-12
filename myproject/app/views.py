from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto,Cliente,Categoria,Orden
from .Forms import ProductoForm,CategoriaForm,OrdenForm,ClienteForm

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

# Crear categoría
@login_required
@permission_required('app.add_categoria', raise_exception=True)
def categoria_crear(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_lista')
    else:
        form = CategoriaForm()
    
    return render(request, 'app/categoria_form.html', {'form': form})

# Lista de categorías
@login_required
@permission_required('app.view_categoria', raise_exception=True)
def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(request, 'app/categoria_lista.html', {'categorias': categorias})

# Eliminar categoría
@login_required
@permission_required('app.delete_categoria', raise_exception=True)
def categoria_eliminar(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_lista')
    return render(request, 'app/categoria_eliminar.html', {'categoria': categoria})

# **Vista para Clientes**

# Crear cliente
@login_required
@permission_required('app.add_cliente', raise_exception=True)
def cliente_crear(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_lista')
    else:
        form = ClienteForm()
    
    return render(request, 'app/cliente_form.html', {'form': form})

# Lista de clientes
@login_required
@permission_required('app.view_cliente', raise_exception=True)
def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/cliente_lista.html', {'clientes': clientes})

# Eliminar cliente
@login_required
@permission_required('app.delete_cliente', raise_exception=True)
def cliente_eliminar(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_lista')
    return render(request, 'app/cliente_eliminar.html', {'cliente': cliente})

# **Vista para Órdenes**

# Crear orden
@login_required
@permission_required('app.add_orden', raise_exception=True)
def orden_crear(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orden_lista')
    else:
        form = OrdenForm()
    
    return render(request, 'app/orden_form.html', {'form': form})

# Lista de órdenes
@login_required
@permission_required('app.view_orden', raise_exception=True)
def orden_lista(request):
    ordenes = Orden.objects.all()
    return render(request, 'app/orden_lista.html', {'ordenes': ordenes})

# Eliminar orden
@login_required
@permission_required('app.delete_orden', raise_exception=True)
def orden_eliminar(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('orden_lista')
    return render(request, 'app/orden_eliminar.html', {'orden': orden})