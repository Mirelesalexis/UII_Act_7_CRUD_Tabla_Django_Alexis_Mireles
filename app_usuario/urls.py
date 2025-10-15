from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('editar/<int:id_usuario>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:id_usuario>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('<int:id_usuario>/', views.detalle_usuario, name='detalle_usuario'), 
]