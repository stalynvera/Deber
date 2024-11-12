from django.urls import path
from . import views

urlpatterns = [
    path('producto_lista/', views.producto_lista, name='producto_lista'),
    path('producto_crear/', views.producto_crear, name='producto_crear'),
    path('producto_eliminar/', views.producto_eliminar, name='producto_eliminar'),
    path('producto_editar/', views.producto_editar_lista, name='producto_editar_lista'),
    path('producto_editar/<int:id>/', views.producto_editar, name='producto_editar'),
    path('categoria_lista/', views.categoria_lista, name='categoria_lista'),
    path('categoria_crear/', views.categoria_crear, name='categoria_crear'),
    path('categoria_eliminar/<int:id>/', views.categoria_eliminar, name='categoria_eliminar'),
    path('cliente_lista/', views.cliente_lista, name='cliente_lista'),
    path('cliente_crear/', views.cliente_crear, name='cliente_crear'),
    path('cliente_eliminar/<int:id>/', views.cliente_eliminar, name='cliente_eliminar'),
    path('orden_lista/', views.orden_lista, name='orden_lista'),
    path('orden_crear/', views.orden_crear, name='orden_crear'),
    path('orden_eliminar/<int:id>/', views.orden_eliminar, name='orden_eliminar'),
]


