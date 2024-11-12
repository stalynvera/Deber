from django.urls import path
from . import views

urlpatterns = [
    path('producto_lista/', views.producto_lista, name='producto_lista'),
    path('producto_crear/', views.producto_crear, name='producto_crear'),
    path('producto_eliminar/', views.producto_eliminar, name='producto_eliminar'),
    path('producto_editar/', views.producto_editar_lista, name='producto_editar_lista'),
    path('producto_editar/<int:id>/', views.producto_editar, name='producto_editar'),
]


