from django.urls import path

from . import views


urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('listar/', views.listar_reservaciones, name='listar'),
    path('crear/', views.crear_reservacion, name='crear'),
    path('editar/<int:id>/', views.editar_reservacion, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_reservicion, name='eliminar'),
]